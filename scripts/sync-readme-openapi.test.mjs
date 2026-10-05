import assert from "node:assert/strict";
import fs from "node:fs";
import http from "node:http";
import os from "node:os";
import path from "node:path";
import { spawn, spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import test from "node:test";

const scripts = path.dirname(fileURLToPath(import.meta.url));
const realGit = spawnSync("which", ["git"], { encoding: "utf8" }).stdout.trim();
const gitEnv = { ...process.env, GIT_AUTHOR_NAME: "Fixture", GIT_AUTHOR_EMAIL: "fixture@example.invalid", GIT_COMMITTER_NAME: "Fixture", GIT_COMMITTER_EMAIL: "fixture@example.invalid" };
const api = { openapi: "3.0.0", paths: { "/api/demo/detail/v1": { get: { operationId: "getDemoDetailV1", tags: ["Demo"], summary: "Detail" } } } };
const operationKey = "GET /api/demo/detail/v1";

function git(cwd, ...args) {
  const result = spawnSync(realGit, args, { cwd, env: gitEnv, encoding: "utf8" });
  assert.equal(result.status, 0, result.stderr);
  return result.stdout.trim();
}

function manifest(root, operationId) {
  fs.mkdirSync(path.join(root, "docs/api-examples"), { recursive: true });
  fs.writeFileSync(path.join(root, `docs/api-examples/${operationId}.json`), "{}\n");
  fs.writeFileSync(path.join(root, "docs/api-examples/manifest.json"), JSON.stringify({ schemaVersion: 1, examples: { [operationKey]: { operationId, file: `docs/api-examples/${operationId}.json` } } }));
}

function fixture(t) {
  const scratch = fs.mkdtempSync(path.join(os.tmpdir(), "readme-sync-test-"));
  t.after(() => fs.rmSync(scratch, { recursive: true, force: true }));
  const root = path.join(scratch, "checkout");
  const remote = path.join(scratch, "remote.git");
  fs.mkdirSync(root);
  git(root, "init", "-b", "main");
  git(scratch, "init", "--bare", remote);
  fs.mkdirSync(path.join(root, "scripts"));
  for (const name of ["update-readme-api-list.mjs", "readme-example-links.mjs", "sync-readme-openapi.mjs"]) {
    fs.copyFileSync(path.join(scripts, name), path.join(root, "scripts", name));
  }
  fs.writeFileSync(path.join(root, "README.md"), "# Fixture\n\n## 服务概览\n\nOld list\n\n## End\nKeep me\n");
  fs.writeFileSync(path.join(root, "README.en.md"), "# Fixture\n\n## Service Overview\n\nOld list\n\n## End\nKeep me\n");
  fs.writeFileSync(path.join(root, "i18n-cache.json"), "{}\n");
  fs.writeFileSync(path.join(root, "glossary.json"), "{}\n");
  manifest(root, "getDemoDetailV1");
  git(root, "add", ".");
  git(root, "commit", "-m", "initial");
  git(root, "remote", "add", "origin", remote);
  git(root, "push", "origin", "HEAD:main");
  const initial = git(root, "rev-parse", "HEAD");
  return { scratch, root, remote, initial };
}

async function service(t) {
  const counts = { spec: 0, translation: 0 };
  const server = http.createServer(async (request, response) => {
    response.setHeader("Content-Type", "application/json");
    if (request.url === "/openapi") {
      counts.spec += 1;
      response.end(JSON.stringify(api));
    } else {
      counts.translation += 1;
      let body = "";
      for await (const chunk of request) body += chunk;
      const batch = JSON.parse(JSON.parse(body).messages.at(-1).content);
      response.end(JSON.stringify({ choices: [{ message: { content: JSON.stringify({ translations: batch.map((text) => `译${text}`) }) } }] }));
    }
  });
  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
  t.after(() => new Promise((resolve) => server.close(resolve)));
  const url = `http://127.0.0.1:${server.address().port}`;
  return { counts, env: { OPENAPI_URL: `${url}/openapi`, OPENAPI_BASIC_AUTH_USER: "fixture", OPENAPI_BASIC_AUTH_PASS: "fixture", DEEPSEEK_BASE_URL: url, DEEPSEEK_API_KEY: "fixture" } };
}

function invoke(root, env, publish = true, nodeArgs = []) {
  return new Promise((resolve, reject) => {
    const child = spawn(process.execPath, [...nodeArgs, path.join(root, "scripts/sync-readme-openapi.mjs"), ...(publish ? ["--publish"] : [])], {
      cwd: root,
      env: { ...gitEnv, README_SYNC_TARGETS: "README.en.md:en,README.md:zh", ...env },
    });
    let stdout = "";
    let stderr = "";
    child.stdout.on("data", (data) => { stdout += data; });
    child.stderr.on("data", (data) => { stderr += data; });
    child.on("error", reject);
    child.on("close", (status) => resolve({ status, stdout, stderr }));
  });
}

function installFetchProbe(f, specUrl, outcomes = []) {
  const preload = path.join(f.scratch, "fetch-probe.mjs");
  const traceFile = path.join(f.scratch, "fetch-trace.json");
  fs.writeFileSync(preload, `
import fs from "node:fs";
const traceFile = ${JSON.stringify(traceFile)};
const specUrl = ${JSON.stringify(specUrl)};
const outcomes = ${JSON.stringify(outcomes)};
const api = ${JSON.stringify(api)};
const trace = { requests: 0, timeouts: [], delays: [] };
const save = () => fs.writeFileSync(traceFile, JSON.stringify(trace));
save();
const timeout = AbortSignal.timeout.bind(AbortSignal);
AbortSignal.timeout = (ms) => { trace.timeouts.push(ms); save(); return timeout(ms); };
const realFetch = globalThis.fetch;
globalThis.fetch = async (url, options) => {
  if (url !== specUrl) return realFetch(url, options);
  trace.requests += 1;
  save();
  const outcome = outcomes.shift() || {};
  if (outcome.timeout) throw new DOMException("Simulated request timeout", "TimeoutError");
  if (outcome.causeCode) throw new TypeError("fetch failed", { cause: { code: outcome.causeCode } });
  const response = new Response(outcome.body ?? JSON.stringify(api), { status: outcome.status ?? 200 });
  if (outcome.bodyTimeout) response.json = async () => { throw new DOMException("Simulated body timeout", "TimeoutError"); };
  return response;
};
const realSetTimeout = globalThis.setTimeout;
globalThis.setTimeout = (callback, ms, ...args) => {
  if (ms === 2000 || ms === 4000) { trace.delays.push(ms); save(); return realSetTimeout(callback, 0, ...args); }
  return realSetTimeout(callback, ms, ...args);
};
`);
  return { nodeArgs: ["--import", preload], trace: () => JSON.parse(fs.readFileSync(traceFile, "utf8")) };
}

function assertUnpublished(f) {
  assert.equal(git(f.root, "rev-parse", "HEAD"), f.initial);
  assert.equal(git(f.root, "--git-dir=" + f.remote, "rev-parse", "main"), f.initial);
  assert.equal(git(f.root, "status", "--porcelain"), "");
  assert.equal((git(f.root, "worktree", "list", "--porcelain").match(/^worktree /gm) || []).length, 1);
}

function installRace(f, competitor = null) {
  const bin = path.join(f.scratch, "bin");
  const countFile = path.join(f.scratch, "push-count");
  fs.mkdirSync(bin);
  fs.writeFileSync(path.join(bin, "git"), `#!${process.execPath}\nconst fs = require('node:fs');\nconst {spawnSync} = require('node:child_process');\nconst args = process.argv.slice(2);\nconst git = ${JSON.stringify(realGit)};\nconst remote = ${JSON.stringify(f.remote)};\nconst countFile = ${JSON.stringify(countFile)};\nconst competitor = ${JSON.stringify(competitor)};\nfunction run(args) { const r = spawnSync(git, args, {encoding:'utf8'}); if(r.status) throw Error(r.stderr); return r.stdout.trim(); }\nif(args[0] === 'push') {\n  const count = fs.existsSync(countFile) ? Number(fs.readFileSync(countFile, 'utf8')) : 0;\n  fs.writeFileSync(countFile, String(count + 1));\n  if(competitor && count === 0) run(['--git-dir='+remote, 'update-ref', 'refs/heads/main', competitor]);\n  if(!competitor) {\n    const parent=run(['--git-dir='+remote, 'rev-parse', 'refs/heads/main']);\n    const tree=run(['--git-dir='+remote, 'rev-parse', parent+'^{tree}']);\n    const commit=run(['--git-dir='+remote, 'commit-tree', tree, '-p', parent, '-m', 'concurrent '+count]);\n    run(['--git-dir='+remote, 'update-ref', 'refs/heads/main', commit]);\n  }\n}\nconst result=spawnSync(git,args,{stdio:'inherit'});\nprocess.exit(result.status ?? 1);\n`, { mode: 0o755 });
  return { PATH: `${bin}:${process.env.PATH}`, countFile };
}

test("preview fetches one snapshot, warms translations once, and leaves the caller and remote untouched", async (t) => {
  const f = fixture(t);
  const server = await service(t);
  fs.appendFileSync(path.join(f.root, "README.md"), "Local draft\n");
  git(f.root, "add", "README.md");
  fs.writeFileSync(path.join(f.root, "untracked.txt"), "private draft\n");
  const status = git(f.root, "status", "--porcelain");
  const staged = git(f.root, "diff", "--cached");
  const result = await invoke(f.root, server.env, false);
  assert.equal(result.status, 0, result.stderr);
  assert.match(result.stdout, /Preview complete/);
  assert.deepEqual(server.counts, { spec: 1, translation: 1 });
  assert.equal(git(f.root, "status", "--porcelain"), status);
  assert.equal(git(f.root, "diff", "--cached"), staged);
  assert.equal(git(f.root, "rev-parse", "HEAD"), f.initial);
  assert.equal(git(f.root, "ls-remote", "origin", "refs/heads/main").split(/\s/)[0], f.initial);
  assert.equal((git(f.root, "worktree", "list", "--porcelain").match(/^worktree /gm) || []).length, 1);
});

test("non-fast-forward rebuild uses the latest manifest and editorial text without translating or fetching the spec twice", async (t) => {
  const f = fixture(t);
  const server = await service(t);
  const other = path.join(f.scratch, "other");
  git(f.scratch, "clone", "--branch", "main", f.remote, other);
  manifest(other, "getDemoLatestV1");
  const readme = path.join(other, "README.md");
  fs.writeFileSync(readme, fs.readFileSync(readme, "utf8").replace("# Fixture", "# Fixture\nConcurrent editorial note"));
  fs.writeFileSync(path.join(other, "i18n-cache.json"), JSON.stringify({ concurrent: "保留并发译文" }));
  git(other, "add", ".");
  git(other, "commit", "-m", "concurrent examples and editorial update");
  const competitor = git(other, "rev-parse", "HEAD");
  git(other, "push", "origin", "HEAD:refs/heads/fixture-competitor");
  const race = installRace(f, competitor);
  fs.appendFileSync(path.join(f.root, "README.md"), "Local draft\n");
  const before = git(f.root, "status", "--porcelain");
  const result = await invoke(f.root, { ...server.env, PATH: race.PATH });
  assert.equal(result.status, 0, result.stderr);
  assert.match(result.stdout, /Published README API lists on attempt 2/);
  assert.deepEqual(server.counts, { spec: 1, translation: 1 });
  assert.equal(fs.readFileSync(race.countFile, "utf8"), "2");
  const finalReadme = git(f.root, "--git-dir=" + f.remote, "show", "main:README.md");
  assert.match(finalReadme, /Concurrent editorial note/);
  assert.match(finalReadme, /getDemoLatestV1\.json/);
  assert.doesNotMatch(finalReadme, /getDemoDetailV1\.json|Local draft/);
  const finalCache = JSON.parse(git(f.root, "--git-dir=" + f.remote, "show", "main:i18n-cache.json"));
  assert.equal(finalCache.concurrent, "保留并发译文");
  assert.equal(Object.keys(finalCache).length, 3);
  assert.equal(git(f.root, "status", "--porcelain"), before);
  assert.equal(git(f.root, "rev-parse", "HEAD"), f.initial);
  assert.equal(git(f.root, "--git-dir=" + f.remote, "rev-list", "--count", "main"), "3");
  const published = git(f.root, "--git-dir=" + f.remote, "rev-parse", "main");
  const repeat = await invoke(f.root, server.env);
  assert.equal(repeat.status, 0, repeat.stderr);
  assert.match(repeat.stdout, /already up to date/);
  assert.deepEqual(server.counts, { spec: 2, translation: 1 });
  assert.equal(git(f.root, "--git-dir=" + f.remote, "rev-parse", "main"), published);
});

test("three advancing-main rejections stop without changing the caller checkout", async (t) => {
  const f = fixture(t);
  const server = await service(t);
  const race = installRace(f);
  const result = await invoke(f.root, { ...server.env, PATH: race.PATH });
  assert.equal(result.status, 1);
  assert.match(result.stderr, /failed after 3 attempts/);
  assert.equal(fs.readFileSync(race.countFile, "utf8"), "3");
  assert.deepEqual(server.counts, { spec: 1, translation: 1 });
  assert.equal(git(f.root, "rev-parse", "HEAD"), f.initial);
  assert.equal(git(f.root, "status", "--porcelain"), "");
  assert.equal((git(f.root, "worktree", "list", "--porcelain").match(/^worktree /gm) || []).length, 1);
});

test("OpenAPI defaults to 60 seconds and preserves a custom timeout", async (t) => {
  const f = fixture(t);
  const server = await service(t);
  const probe = installFetchProbe(f, server.env.OPENAPI_URL);
  for (const timeout of [undefined, "1234"]) {
    const result = await invoke(f.root, { ...server.env, OPENAPI_FETCH_TIMEOUT_MS: timeout }, false, probe.nodeArgs);
    assert.equal(result.status, 0, result.stderr);
    assert.deepEqual(probe.trace(), { requests: 1, timeouts: [timeout ? 1234 : 60000], delays: [] });
    assertUnpublished(f);
  }
});

test("OpenAPI request and body timeouts recover on the next attempt", async (t) => {
  const f = fixture(t);
  const server = await service(t);
  for (const outcome of [{ timeout: true }, { bodyTimeout: true }]) {
    const probe = installFetchProbe(f, server.env.OPENAPI_URL, [outcome]);
    const result = await invoke(f.root, server.env, false, probe.nodeArgs);
    assert.equal(result.status, 0, result.stderr);
    assert.deepEqual(probe.trace(), { requests: 2, timeouts: [60000, 60000], delays: [2000] });
    assert.match(result.stderr, /attempt 2\/3/);
    assertUnpublished(f);
  }
});

test("two OpenAPI timeouts recover on the third attempt with 2 and 4 second backoff", async (t) => {
  const f = fixture(t);
  const server = await service(t);
  const probe = installFetchProbe(f, server.env.OPENAPI_URL, [{ timeout: true }, { timeout: true }]);
  const result = await invoke(f.root, server.env, false, probe.nodeArgs);
  assert.equal(result.status, 0, result.stderr);
  assert.deepEqual(probe.trace(), { requests: 3, timeouts: [60000, 60000, 60000], delays: [2000, 4000] });
  assertUnpublished(f);
});

test("three OpenAPI timeouts stop before translating or publishing", async (t) => {
  const f = fixture(t);
  const server = await service(t);
  const probe = installFetchProbe(f, server.env.OPENAPI_URL, Array.from({ length: 3 }, () => ({ timeout: true })));
  const result = await invoke(f.root, server.env, true, probe.nodeArgs);
  assert.equal(result.status, 1);
  assert.match(result.stderr, /Simulated request timeout/);
  assert.deepEqual(probe.trace(), { requests: 3, timeouts: [60000, 60000, 60000], delays: [2000, 4000] });
  assert.deepEqual(server.counts, { spec: 0, translation: 0 });
  assertUnpublished(f);
});

test("Undici connection, header, and body timeout causes are retried", async (t) => {
  const f = fixture(t);
  const server = await service(t);
  for (const causeCode of ["UND_ERR_CONNECT_TIMEOUT", "UND_ERR_HEADERS_TIMEOUT", "UND_ERR_BODY_TIMEOUT"]) {
    const probe = installFetchProbe(f, server.env.OPENAPI_URL, [{ causeCode }]);
    const result = await invoke(f.root, server.env, false, probe.nodeArgs);
    assert.equal(result.status, 0, result.stderr);
    assert.deepEqual(probe.trace(), { requests: 2, timeouts: [60000, 60000], delays: [2000] });
    assertUnpublished(f);
  }
});

test("HTTP and JSON errors are not retried or published", async (t) => {
  const f = fixture(t);
  const server = await service(t);
  for (const outcome of [{ status: 401 }, { status: 503 }, { body: "not JSON" }]) {
    const probe = installFetchProbe(f, server.env.OPENAPI_URL, [outcome]);
    const result = await invoke(f.root, server.env, true, probe.nodeArgs);
    assert.equal(result.status, 1);
    assert.deepEqual(probe.trace(), { requests: 1, timeouts: [60000], delays: [] });
    assert.deepEqual(server.counts, { spec: 0, translation: 0 });
    assertUnpublished(f);
  }
});

test("non-timeout transport errors are not retried", async (t) => {
  const f = fixture(t);
  const server = await service(t);
  const probe = installFetchProbe(f, server.env.OPENAPI_URL, [{ causeCode: "ECONNRESET" }]);
  const result = await invoke(f.root, server.env, true, probe.nodeArgs);
  assert.equal(result.status, 1);
  assert.deepEqual(probe.trace(), { requests: 1, timeouts: [60000], delays: [] });
  assertUnpublished(f);
});

test("invalid OpenAPI timeout values fail before fetching or publishing", async (t) => {
  const f = fixture(t);
  const server = await service(t);
  const probe = installFetchProbe(f, server.env.OPENAPI_URL);
  for (const timeout of ["0", "-1", "NaN", "Infinity"]) {
    const result = await invoke(f.root, { ...server.env, OPENAPI_FETCH_TIMEOUT_MS: timeout }, true, probe.nodeArgs);
    assert.equal(result.status, 1);
    assert.match(result.stderr, /Invalid OPENAPI_FETCH_TIMEOUT_MS/);
    assert.deepEqual(probe.trace(), { requests: 0, timeouts: [], delays: [] });
    assertUnpublished(f);
  }
});

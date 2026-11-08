from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("package_setup", ROOT / "setup.py")
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
transform = MODULE.pypi_long_description


@pytest.mark.parametrize("host", ["justoneapi.com", "docs.justoneapi.com", "dashboard.justoneapi.com"])
@pytest.mark.parametrize("wrapper", ["{}", "[文档]({})", '<a href="{}">Docs</a>', "<{}>"])
def test_changes_only_source_on_owned_navigation_links(host, wrapper):
    url = f"https://{host}/zh/api/demo?utm_source=github.com&utm_campaign=keep%20this&x=1&x=2#fragment"
    original = wrapper.format(url)
    assert transform(original) == original.replace("utm_source=github.com", "utm_source=pypi.org")


@pytest.mark.parametrize("url", [
    "https://github.com/justoneapi-official/justoneapi-python?utm_source=github.com",
    "https://api.justoneapi.com/api/demo?utm_source=github.com",
    "https://docs.justoneapi.com.evil.invalid/?utm_source=github.com",
    "https://fakejustoneapi.com/?utm_source=github.com",
    "https://docs.justoneapi.com:8443/?utm_source=github.com",
    "https://docs.justoneapi.com:bad/?utm_source=github.com",
    "https://someone@docs.justoneapi.com/?utm_source=github.com",
    "http://docs.justoneapi.com/?utm_source=github.com",
    "https://docs.justoneapi.com/?utm_source=github.com&utm_source=github.com",
    "https://docs.justoneapi.com/?utm_source=github.com&utm%5Fsource=other",
    "https://docs.justoneapi.com/?utm_source=",
    "https://docs.justoneapi.com/?utm_source=pypi.org",
    "https://docs.justoneapi.com/?utm_source=other",
    "https://docs.justoneapi.com/?campaign=github.com#utm_source=github.com",
    "https://docs.justoneapi.com/#fragment?utm_source=github.com",
    "https://docs.justoneapi.com/assets/logo.png",
])
def test_does_not_relabel_other_or_ambiguous_urls(url):
    assert transform(url) == url


def test_preserves_query_encoding_order_and_html_escaping():
    original = 'https://DOCS.justoneapi.com:443/zh/?x=%2f&amp;utm%5fsource=%67ithub.com&amp;utm_content=repo_readme#anchor'
    assert transform(original) == original.replace("%67ithub.com", "pypi.org")


def test_repository_readmes_are_unchanged_and_pypi_render_is_repeatable():
    before = {name: (ROOT / name).read_bytes() for name in ["README.md", "README.en.md", "README.zh-CN.md"]}
    source = before["README.md"].decode("utf-8")
    rendered = transform(source)
    assert rendered != source
    assert rendered == source.replace("utm_source=github.com", "utm_source=pypi.org")
    assert transform(rendered) == rendered
    assert before == {name: (ROOT / name).read_bytes() for name in before}

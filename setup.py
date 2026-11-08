"""Keep repository READMEs intact while identifying PyPI description links."""

from pathlib import Path
import re
from urllib.parse import unquote_plus, urlsplit


_URL = re.compile(r"https://[^\s<>\"'`\[\](){}]+", re.IGNORECASE)
_NAVIGATION_HOSTS = {"justoneapi.com", "docs.justoneapi.com", "dashboard.justoneapi.com"}


def pypi_long_description(readme: str) -> str:
    """Replace one unambiguous GitHub source on owned navigation URLs only."""

    def replace(match: re.Match[str]) -> str:
        url = match.group()
        try:
            parsed = urlsplit(url)
            if (not parsed.query or parsed.hostname not in _NAVIGATION_HOSTS or parsed.port not in (None, 443)
                    or parsed.username is not None or parsed.password is not None):
                return url
        except ValueError:
            return url

        prefix, question, tail = url.partition("?")
        if not question:
            return url
        query, hash_mark, fragment = tail.partition("#")
        fields = re.split(r"(&amp;|&)", query)
        sources = []
        for index in range(0, len(fields), 2):
            key, equals, value = fields[index].partition("=")
            if unquote_plus(key) == "utm_source":
                sources.append((index, key, unquote_plus(value)))
        if len(sources) != 1 or sources[0][2] != "github.com":
            return url
        index, key, _ = sources[0]
        fields[index] = key + "=pypi.org"
        return prefix + question + "".join(fields) + hash_mark + fragment

    return _URL.sub(replace, readme)


if __name__ == "__main__":
    from setuptools import setup

    setup(
        long_description=pypi_long_description(
            Path(__file__).with_name("README.md").read_text(encoding="utf-8")
        ),
        long_description_content_type="text/markdown",
    )

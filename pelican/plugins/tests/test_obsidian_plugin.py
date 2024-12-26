from pathlib import Path

import pytest
from pelican.plugins.obsidian import ObsidianMarkdownReader  # noqa


@pytest.fixture
def obsidian(path):
    omr = ObsidianMarkdownReader(
        settings={
            "MARKDOWN": {
                "extensions": [
                    "markdown.extensions.extra",
                    "markdown.extensions.meta",
                ]
            },
            "FORMATTED_FIELDS": ["summary"],
        }
    )
    cwd = Path.cwd()
    source_path = cwd / "pelican" / "plugins" / "tests" / f"fixtures/{path}.md"
    obsidian = omr.read(source_path)
    return obsidian


@pytest.mark.parametrize('path', ["tags"])
def test_tags_works_correctly(obsidian):
    """Tags formatted as yaml list works properly"""
    content, meta = obsidian
    tags = meta["tags"]

    assert 'Some text here' in content
    assert len(tags) == 3
    assert 'python' == tags[0].name
    assert 'code-formatter' == tags[1].name
    assert 'black' == tags[2].name


@pytest.mark.parametrize('path', ["tags_comma"])
def test_tags_works_pelican_way(obsidian):
    """Test normal tags"""
    content, meta = obsidian
    tags = meta["tags"]

    assert 'Some text here' in content
    assert len(meta["tags"]) == 3
    assert 'python' == tags[0].name
    assert 'code-formatter' == tags[1].name
    assert 'black' == tags[2].name


@pytest.mark.parametrize('path', ["other_list_type"])
def test_other_list_property(obsidian):
    """List is preserved for other list type property"""
    content, meta = obsidian

    assert 'Some text here' in content
    assert len(meta["other"]) == 4


@pytest.mark.parametrize('path', ["internal_link"])
def test_internal_link_not_seen_in_article(obsidian):
    """
    If linked article has not been processed earlier
    content is not linked.
    """
    content, meta = obsidian
    assert '<p>tags</p>' == content


@pytest.mark.parametrize('path', ["internal_link"])
def test_external_link(obsidian):
    """Able to use normal markdown links which renders properly"""
    content, meta = obsidian
    assert '<a href="https://example.com">external</a>'


@pytest.mark.parametrize('path', ["colon_in_prop"])
def test_colon_in_prop(obsidian):
    """Using a colon in prop should not mess with string formatting"""
    content, meta = obsidian
    assert meta["title"] == 'Hello: There'


def test_with_generator():
    pass

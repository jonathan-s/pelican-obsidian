from pathlib import Path

import pytest
from pelican.generators import ArticlesGenerator
from pelican.tests.support import get_settings
from pelican.plugins.obsidian import ObsidianMarkdownReader, populate_files_and_articles  # noqa


@pytest.fixture
def obsidian(path):
    settings = get_settings()
    settings["DEFAULT_CATEGORY"] = "Default"
    settings["DEFAULT_DATE"] = (1970, 1, 1)
    settings["READERS"] = {"asc": None}
    settings["CACHE_CONTENT"] = False
    omr = ObsidianMarkdownReader(
        settings=settings
    )
    cwd = Path.cwd()
    source_path = cwd / "pelican" / "plugins" / "tests" / f"fixtures/{path}.md"
    generator = ArticlesGenerator(
        context=settings,
        settings=settings,
        path=cwd / "pelican" / "plugins" / "tests" / "fixtures",
        theme=settings["THEME"],
        output_path=None,
    )
    populate_files_and_articles(generator)
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
    assert len(meta["other"]) == 3


@pytest.mark.parametrize('path', ["unknown_internal_link"])
def test_internal_link_not_seen_in_article(obsidian):
    """
    If linked article has not been processed earlier
    content is not linked.
    """
    content, meta = obsidian
    assert '<p>great-article-not-exist</p>' == content

@pytest.mark.parametrize('path', ["internal_link"])
def test_internal_link_in_article(obsidian):
    """
    If linked article has internal link, it should be linked
    """
    content, meta = obsidian
    assert '<p><a href="{filename}/tags.md">tags</a></p>' == content

@pytest.mark.parametrize('path', ["internal_image"])
def test_internal_image_in_article(obsidian):
    """
    If linked article has internal image, it should be linked
    """
    content, meta = obsidian
    assert '<p><img alt="pelican-in-rock.webp" src="{static}/assets/images/pelican-in-rock.webp"></p>' == content


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

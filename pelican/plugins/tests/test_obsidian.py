from plugins.obsidian import ObsidianMarkdownReader
from pelican.utils import pelican_open

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

source_path = "fixtures/black_yapf.md"
omr.read(source_path)
with pelican_open(source_path) as text:
    text = omr.remove_non_existing_breadcrumbs(text)
    text = omr.replace_obsidian_links(text)
    content = omr._md.convert(text)
    pass

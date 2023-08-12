import os
import re
from itertools import chain
from pathlib import Path

from markdown import Markdown
from pelican import signals
from pelican.readers import MarkdownReader
from pelican.utils import pelican_open

ARTICLE_PATH = {}
ARTICLE_TITLE = {}
FILE_PATH = {}

# Regex for links. The first group is the filename, the second is the linkname.
# The linkname is optional. If it is not present, the filename is used.
# e.g. [[my link]] -> filename: my link, linkname: my link
# e.g. [[ my work | is finished ]] -> filename: my work, linkname: is finished
link = r"\[\[\s*(?P<filename>[^|\]]+)(\|\s*(?P<linkname>.+))?\]\]"
file_re = re.compile(f"!{link}")
link_re = re.compile(link)
title_re = re.compile(r"(?i)title: (.*)")

# Regex for the extracting link with the X:: prefix.
# X::[[asdae]] syntax, which is used to create a link to a file
# X:: [[dfges]] and X::[[myfsew|dfgwerf]], x::[[ddfgd]] and x::[[dfg|ersdf]]
# are all valid.
x_element_re = re.compile(rf"(?i)X::\s*{link}")
up_element_re = re.compile(rf"(?i)Up::\s*{link}")
down_element_re = re.compile(rf"(?i)Down::\s*{link}")
"""
# Test cases for the link regex
[[my link]]
[[ my work ]]
[[ my work | is finished ]]

# Test cases for the file regex
![[ a file.jpg ]]
![[file.jpg]]
"""


def get_file_and_linkname(match: re.Match):
    """Get the filename and linkname (visible label) from the match object.

    e.g. [[my link]] -> filename: my link, linkname: my link
    e.g. [[ my work | is finished ]] -> filename: my work, linkname: is finished

    Args:
        match (re.Match): The match object from the regex.

    Returns:
        tuple: The filename and linkname.
    """
    group = match.groupdict()
    filename = group["filename"].strip()
    linkname = group["linkname"] or filename
    linkname = linkname.strip()
    return filename, linkname


def link_replacement(match: re.Match) -> str:
    """Replace the link with the correct path.

    Args:
        match (re.Match): The match object from the regex.

    Returns:
        str: The replacement string.

    Example:
        link:
        [[a_link]] -> [a_link]({{filename}}/a_link.md)
    """
    filename, linkname = get_file_and_linkname(match)
    # get the path of the article defined by filename
    path = ARTICLE_PATH.get(filename)
    title = ARTICLE_TITLE.get(filename, filename)
    if path:
        link_structure = f"[{title}]({{filename}}{path}{filename}.md)"
        # logger.debug(
        #     f"Found link: {linkname} | {title}, replacing with: {link_structure}"
        # )
    else:
        link_structure = f"{linkname}"
        # logger.debug(f"No article found for filename {filename}")
    return link_structure


def file_replacement(match: re.Match) -> str:
    """Replace the file link with the correct path.

    Args:
        match (re.Match): The match object from the regex.

    Returns:
        str: The replacement string.

    Example:
        image:
        ![[a file.jpg]] -> ![a file.jpg]({{static}}/images/a file.jpg)
    """
    filename, linkname = get_file_and_linkname(match)
    if path := FILE_PATH.get(filename):
        link_structure = "![{linkname}]({{static}}{path}{filename})".format(
            linkname=linkname, path=path, filename=filename
        )
        # logger.debug(f"Link structure: {link_structure} for {filename}")
    else:
        # don't show it at all since it will be broken
        link_structure = ""

    return link_structure


def breadcrumb_replacement(b_match: re.Match) -> str:
    """Remove the X::[[a_link]] element when the path for the link is not found.

    Args:
        b_match (re.Match): The match for the `X::[[a_link]]`-like element

    Returns:
        str: The replacement string.

    Example:
        X::[[a_link]] -> ERASED
        up::[[MOC_Python]] -> ERASED
    """
    if match := link_re.search(str(b_match.group())):
        # get first group of the match
        filename, _ = get_file_and_linkname(match)
        # get the path of the article defined by filename

        path = ARTICLE_PATH.get(filename)
        if not path:
            # logger.debug(f"Erase: {b_match.group()}")
            return ""
        else:
            if b_match:
                # keep the element
                return b_match.group()


class ObsidianMarkdownReader(MarkdownReader):
    """Change the format of various links to the accepted case of pelican."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def replace_obsidian_links(text):
        text = file_re.sub(file_replacement, text)
        text = link_re.sub(link_replacement, text)
        return text

    @staticmethod
    def remove_non_existing_breadcrumbs(text):
        text = x_element_re.sub(breadcrumb_replacement, text)
        text = up_element_re.sub(breadcrumb_replacement, text)
        text = down_element_re.sub(breadcrumb_replacement, text)
        return text

    def read(self, source_path):
        """
        Parse content and metadata of markdown files. Also changes the links to the acceptable format for pelican
        """
        self._source_path = source_path
        self._md = Markdown(**self.settings["MARKDOWN"])

        # logger.info(f"Reading file: {source_path}")
        with pelican_open(source_path) as text:
            text = self.remove_non_existing_breadcrumbs(text)
            text = self.replace_obsidian_links(text)
            content = self._md.convert(text)

        if hasattr(self._md, "Meta"):
            metadata = self._parse_metadata(self._md.Meta)
        else:
            metadata = {}

        return content, metadata


def populate_files_articles_titles(article_generator):
    """Populate the ARTICLE_PATH, FILE_PATH and ARTICLE_TITLE.

    ARTICLE_PATH: {filename: path}
    E.g. {"my-article": "notes/"} for the article "notes/my-article.md"

    FILE_PATH: {filename: path}
    E.g. {"my-image.jpg": "images/"} for the file "images/my-image.jpg"

    ARTICLE_TITLE: {filename: title}
    E.g. {"my-article": "My Article"} for the article "notes/my-article.md"
    """
    global ARTICLE_PATH
    global FILE_PATH
    global ARTICLE_TITLE

    base_path = Path(article_generator.path)
    articles = base_path.glob("**/*.md")
    for article in articles:
        full_path, filename_w_ext = os.path.split(article)
        filename, ext = os.path.splitext(filename_w_ext)
        path = str(full_path).replace(str(base_path), "") + "/"
        ARTICLE_PATH[filename] = path
        # logger.debug(f"ARTICLE: {filename} -> {path}")

        # get the title of the article from the frontmatter
        # open the file and get the title
        with open(article) as f:
            content = f.read()
            # find the title text. The key should be case insensitive,
            # i.e. all: Title, TITLE, title should work
            title = re.search(title_re, content)

        if title is None:
            title = filename
        else:
            title = title.group(1).strip()

        # logger.debug(f"Found internal link to article: {filename}, title: {title}")
        ARTICLE_TITLE[filename] = title

    globs = [
        base_path.glob(f"**/*.{ext}") for ext in ["png", "jpg", "svg", "apkg", "gif"]
    ]
    files = chain(*globs)
    for _file in files:
        full_path, filename_w_ext = os.path.split(_file)
        path = str(full_path).replace(str(base_path), "") + "/"
        FILE_PATH[filename_w_ext] = path


def modify_reader(article_generator):
    """Modify the reader to use the ObsidianMarkdownReader.

    Before generating the articles, run the content through the ObsidianMarkdownReader.
    for replacing the obsidian links to the desired format.
    """
    populate_files_articles_titles(article_generator)
    article_generator.readers.readers["md"] = ObsidianMarkdownReader(
        article_generator.settings
    )


def modify_metadata(article_generator, metadata: dict) -> None:
    """Modify the tags, so we can define the tags as we are used to in obsidian.

    Args:
        article_generator (ArticleGenerator): The article generator.
        metadata (dict): The metadata of the article.
    """
    for tag in metadata.get("tags", []):
        if "#" in tag.name:
            tag.name = tag.name.replace("#", "")


def register():
    """Register the plugin in pelican."""
    signals.article_generator_context.connect(modify_metadata)
    signals.article_generator_init.connect(modify_generator)

    signals.page_generator_context.connect(modify_metadata)
    signals.page_generator_init.connect(modify_generator)


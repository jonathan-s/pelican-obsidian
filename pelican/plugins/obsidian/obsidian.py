from pathlib import Path

from itertools import chain
import os
import re
from pelican import signals
from pelican.readers import MarkdownReader
from pelican.utils import pelican_open

from markdown import Markdown

ARTICLE_PATHS = {}
FILE_PATHS = {}

link = r'\[\[\s*(?P<filename>[\w+\s.]+)(\|\s*(?P<linkname>[\w\s]+))?\]\]'
file_re = re.compile(r'!' + link)
link_re = re.compile(link)


"""
# Test cases
[[my link]]
[[ my work ]]
[[ my work | is finished ]]

![[ a file.jpg ]]
![[file.jpg]]
"""


def get_file_and_linkname(match):
    group = match.groupdict()
    filename = group['filename'].strip()
    linkname = group['linkname'] if group['linkname'] else filename
    linkname = linkname.strip()
    return filename, linkname


class ObsidianMarkdownReader(MarkdownReader):
    """
    Change the format of various links to the accepted case of pelican.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def replace_obsidian_links(self, text):
        def link_replacement(match):
            filename, linkname = get_file_and_linkname(match)
            path = ARTICLE_PATHS.get(filename)
            if path:
                link_structure = '[{linkname}]({{filename}}{path}{filename}.md)'.format(
                    linkname=linkname, path=path, filename=filename
                )
            else:
                link_structure = '{linkname}'.format(linkname=linkname)
            return link_structure

        def file_replacement(match):
            filename, linkname = get_file_and_linkname(match)
            path = FILE_PATHS.get(filename)
            if path:
                link_structure = '![{linkname}]({{static}}{path}{filename})'.format(
                    linkname=linkname, path=path, filename=filename
                )
            else:
                # don't show it at all since it will be broken
                link_structure = ''
            return link_structure

        text = file_re.sub(file_replacement, text)
        text = link_re.sub(link_replacement, text)
        return text

    def read(self, source_path):
        """Parse content and metadata of markdown files

        It also changes the links to the acceptable format for pelican
        """

        self._source_path = source_path
        self._md = Markdown(**self.settings['MARKDOWN'])

        with pelican_open(source_path) as text:
            text = self.replace_obsidian_links(text)
            content = self._md.convert(text)

        if hasattr(self._md, 'Meta'):
            metadata = self._parse_metadata(self._md.Meta)
        else:
            metadata = {}
        return content, metadata


def populate_files_and_articles(article_generator):
    global ARTICLE_PATHS
    global FILE_PATHS

    base_path = Path(article_generator.path)
    articles = base_path.glob('**/*.md')
    for article in articles:
        full_path, filename_w_ext = os.path.split(article)
        filename, ext = os.path.splitext(filename_w_ext)
        path = str(full_path).replace(str(base_path), '') + '/'
        ARTICLE_PATHS[filename] = path

    globs = [base_path.glob('**/*.{}'.format(ext)) for ext in ['png', 'jpg', 'svg', 'apkg', 'gif']]
    files = chain(*globs)

    for _file in files:
        full_path, filename_w_ext = os.path.split(_file)
        path = str(full_path).replace(str(base_path), '') + '/'
        FILE_PATHS[filename_w_ext] = path


def modify_reader(article_generator):
    populate_files_and_articles(article_generator)
    article_generator.readers.readers['md'] = ObsidianMarkdownReader(article_generator.settings)


def modify_metadata(article_generator, metadata):
    """
    Modify the tags so we can define the tags as we are used to in obsidian.
    """
    for tag in metadata.get('tags', []):
        if '#' in tag.name:
            tag.name = tag.name.replace('#', '')


def register():
    signals.article_generator_context.connect(modify_metadata)
    signals.article_generator_init.connect(modify_reader)

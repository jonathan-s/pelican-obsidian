from pelican import signals


def pre_taxonomy(article_generator):
    """
    Modify the tags of the article
    """
    pass


def modify_article_content(article_generator, content):
    """
    Change the format of various links to the accepted case of pelican.
    """
    pass


def modify_metadata(article_generator, context):
    """
    Modify the metadata
    """
    pass


def register():
    signals.article_generator_context.connect(modify_metadata)
    signals.article_generator_pretaxonomy.connect(pre_taxonomy)
    signals.article_generator_write_article.connect(modify_article_content)

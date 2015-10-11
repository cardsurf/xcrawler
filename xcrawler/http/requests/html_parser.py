
from lxml.etree import HTMLParser


class HtmlParserFactory(object):
    """Creates an instance of the HTMLParser class.

    """
    def __init__(self):
        pass

    def create_html_parser_unicode(self):
        unicode_parser = HTMLParser(encoding="utf-8")
        return unicode_parser


from lxml.etree import HTMLParser

class HtmlParserFactory:
    """Creates a converter that convert an instance of one type to a specified type.

    """

    def __init__(self):
        pass

    def create_html_parser_unicode(self):
        unicode_parser = HTMLParser(encoding="utf-8")
        return unicode_parser

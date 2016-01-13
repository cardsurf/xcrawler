from lxml.etree import HTML

from xcrawler.pythonutils.types.instance_resolver import InstanceResolver
from xcrawler.http.requests.html_parser import HtmlParserFactory
from xcrawler.core.extractor.element import ElementFactory


class StringConverter(object):
    """Converts a string to a specified type.

    """
    def __init__(self,
                 instance_resolver=InstanceResolver(),
                 html_parser_factory=HtmlParserFactory(),
                 element_factory=ElementFactory()):
        self.instance_resolver = instance_resolver
        self.html_parser_factory = html_parser_factory
        self.element_factory = element_factory

    def convert_to_byte_string_utf8(self, string):
        if self.instance_resolver.is_byte_string(string):
            return string
        byte_string_utf8 = string.encode("utf-8")
        return byte_string_utf8

    def convert_to_unicode_string(self, string):
        if self.instance_resolver.is_unicode_string(string):
            return string
        unicode_string = string.decode('utf8')
        return unicode_string

    def convert_to_tree_elements(self, html_string):
        tree_elements = self.element_factory.create_element("Root")
        if len(html_string) > 0:
            unicode_parser = self.html_parser_factory.create_html_parser_unicode()
            tree_elements = HTML(html_string, parser=unicode_parser)
        return tree_elements
    
    def list_convert_to_unicode_string(self, list_strings):
        return [self.convert_to_unicode_string(s) for s in list_strings]

    def list_convert_to_byte_string_utf8(self, list_strings):
        return [self.convert_to_byte_string_utf8(s) for s in list_strings]


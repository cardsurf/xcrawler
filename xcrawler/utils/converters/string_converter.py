
from lxml.etree import HTML

from xcrawler.utils.types.instance_resolver import InstanceResolver
from xcrawler.utils.converters.converter_factory import ConverterFactory


class StringConverter:
    """Converts a string to a specified type.

    """
    def __init__(self,
                 instance_resolver=InstanceResolver(),
                 converter_factory=ConverterFactory()):
        self.instance_resolver = instance_resolver
        self.converter_factory = converter_factory

    def convert_to_byte_string_utf8(self, string):
        unicode_string = self.convert_to_unicode_string(string)
        byte_string_utf8 = unicode_string.encode("utf-8")
        return byte_string_utf8

    def convert_to_unicode_string(self, string):
        if self.instance_resolver.is_unicode_string(string):
            return string
        unicode_string = string.decode('utf8')
        return unicode_string

    def convert_to_tree_elements(self, html_string):
        unicode_parser = self.converter_factory.create_html_parser_unicode()
        tree_elements = HTML(html_string, parser=unicode_parser)
        return tree_elements
    
    def list_convert_to_unicode_string(self, list_strings):
        return [self.convert_to_unicode_string(s) for s in list_strings]

    def list_convert_to_byte_string_utf8(self, list_strings):
        return [self.convert_to_byte_string_utf8(s) for s in list_strings]


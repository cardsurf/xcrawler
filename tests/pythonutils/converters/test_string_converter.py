import unittest

import mock
from lxml.etree import HTMLParser
from lxml.etree import Element

from xcrawler.pythonutils.converters.string_converter import StringConverter
from xcrawler.pythonutils.types.instance_resolver import InstanceResolver
from xcrawler.http.requests.html_parser import HtmlParserFactory


class TestStringConverter(unittest.TestCase):

    def setUp(self):
        instance_resolver = mock.create_autospec(InstanceResolver).return_value
        converter_factory = mock.create_autospec(HtmlParserFactory).return_value
        self.string_converter = StringConverter(instance_resolver, converter_factory)

    @mock.patch.object(StringConverter, 'convert_to_unicode_string')
    def test_convert_to_byte_string_utf8(self, mock_convert_to_unicode_string):
        mock_string = "mock"
        mock_unicode_string = u"mock"
        mock_convert_to_unicode_string.return_value = mock_unicode_string
        result = self.string_converter.convert_to_byte_string_utf8(mock_string)
        self.assertEquals(result, b"mock")

    def test_convert_to_unicode_string_argument_unicode_string(self):
        mock_string = u"mock"
        self.string_converter.instance_resolver.is_unicode_string.return_value = True
        result = self.string_converter.convert_to_unicode_string(mock_string)
        self.assertEquals(result, mock_string)

    @mock.patch('xcrawler.pythonutils.converters.string_converter.HTML')
    def test_convert_to_tree_elements(self, mock_html_function):
        mock_html_string = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        mock_unicode_parser = mock.create_autospec(HTMLParser).return_value
        mock_tree_elements = mock.create_autospec(Element).return_value
        self.string_converter.html_parser_factory.create_html_parser_unicode.return_value = mock_unicode_parser
        mock_html_function.return_value = mock_tree_elements
        result = self.string_converter.convert_to_tree_elements(mock_html_string)
        self.assertEquals(result, mock_tree_elements)

    def test_convert_to_unicode_string_argument_byte_string_utf8(self):
        mock_string = b"mock"
        self.string_converter.instance_resolver.is_unicode_string.return_value = False
        result = self.string_converter.convert_to_unicode_string(mock_string)
        self.assertEquals(result, u"mock")

    def test_list_convert_string_to_byte_string_utf8(self):
        list_strings = ["mock1", b"mock2", u"mock3"]
        result = self.string_converter.list_convert_to_byte_string_utf8(list_strings)
        self.assertEquals(result, [b"mock1", b"mock2", b"mock3"])

    def test_list_convert_string_to_unicode_string(self):
        list_strings = ["mock1", b"mock2", u"mock3"]
        result = self.string_converter.list_convert_to_unicode_string(list_strings)
        self.assertEquals(result, [u"mock1", u"mock2", u"mock3"])


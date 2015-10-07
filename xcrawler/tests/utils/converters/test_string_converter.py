

import unittest
import mock

from xcrawler.utils.converters.string_converter import StringConverter


class TestStringConverter(unittest.TestCase):

    def setUp(self):
        self.string_converter = StringConverter()

    @mock.patch.object(StringConverter, 'convert_to_unicode_string')
    def test_convert_to_byte_string_utf8(self, mock_convert_to_unicode_string):
        mock_string = "mock"
        mock_unicode_string = u"mock"
        mock_convert_to_unicode_string.return_value = mock_unicode_string
        result = self.string_converter.convert_to_byte_string_utf8(mock_string)
        self.assertEquals(result, b"mock")

    @mock.patch('xcrawler.utils.converters.string_converter.string_utils.is_unicode_string')
    def test_convert_to_unicode_string_argument_unicode_string(self, mock_is_unicode_string):
        mock_string = u"mock"
        mock_is_unicode_string.return_value = True
        result = self.string_converter.convert_to_unicode_string(mock_string)
        self.assertEquals(result, mock_string)

    @mock.patch('xcrawler.utils.converters.string_converter.string_utils.is_unicode_string')
    def test_convert_to_unicode_string_argument_byte_string_utf8(self, mock_is_unicode_string):
        mock_string = b"mock"
        mock_is_unicode_string.return_value = False
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


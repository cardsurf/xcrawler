

import unittest
import mock

from xcrawler.utils.converters.object_converter import ObjectConverter


class TestObjectConverter(unittest.TestCase):

    def setUp(self):
        self.object_converter = ObjectConverter()

    @mock.patch('xcrawler.utils.converters.object_converter.string_utils.convert_string_to_byte_string_utf8')
    @mock.patch.object(ObjectConverter, 'convert_to_string')
    def test_convert_to_byte_string_utf8(self, mock_convert_to_string, mock_convert_string_to_byte_string_utf8):
        mock_object = mock.Mock()
        mock_object_string = "mock object"
        mock_object_byte_string_utf8 = b"mock object"
        mock_convert_to_string.return_value = mock_object_string
        mock_convert_string_to_byte_string_utf8.return_value = mock_object_byte_string_utf8
        result = self.object_converter.convert_to_byte_string_utf8(mock_object)
        self.assertEquals(result, mock_object_byte_string_utf8)

    @mock.patch('xcrawler.utils.converters.object_converter.string_utils.convert_string_to_unicode_string')
    @mock.patch.object(ObjectConverter, 'convert_to_string')
    def test_convert_to_unicode_string(self, mock_convert_to_string, mock_convert_string_to_unicode_string):
        mock_object = mock.Mock()
        mock_object_string = "mock object"
        mock_object_unicode_string = u"mock object"
        mock_convert_to_string.return_value = mock_object_string
        mock_convert_string_to_unicode_string.return_value = mock_object_unicode_string
        result = self.object_converter.convert_to_unicode_string(mock_object)
        self.assertEquals(result, mock_object_unicode_string)

    @mock.patch('xcrawler.utils.converters.object_converter.string_utils.is_byte_string')
    def test_convert_to_string_argument_object(self, mock_is_byte_string):
        mock_object = mock.Mock()
        mock_str = mock.Mock()
        mock_str.return_value = "mock_object"
        mock_object.__str__ = mock_str
        mock_is_byte_string.return_value = False
        result = self.object_converter.convert_to_string(mock_object)
        self.assertEquals(result, "mock_object")

    @mock.patch('xcrawler.utils.converters.object_converter.string_utils.is_byte_string')
    def test_convert_to_string_argument_byte_string(self, mock_is_byte_string):
        mock_object = b"mock object"
        mock_is_byte_string.return_value = True
        result = self.object_converter.convert_to_string(mock_object)
        self.assertEquals(result, mock_object)

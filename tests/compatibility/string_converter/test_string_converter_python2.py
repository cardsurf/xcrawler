
import unittest
import mock

from xcrawler.compatibility.string_converter.string_converter_python2 import StringConverterPython2


class TestStringConverterPython2(unittest.TestCase):

    def setUp(self):
        self.string_converter = StringConverterPython2()

    @mock.patch.object(StringConverterPython2, 'convert_to_byte_string_utf8')
    def test_convert_to_string_argument_byte_string(self, mock_convert_to_byte_string_utf8):
        mock_string = b"mock"
        mock_byte_string = b"mock"
        mock_convert_to_byte_string_utf8.return_value = mock_byte_string
        result = self.string_converter.convert_to_string(mock_string)
        self.assertEquals(result, mock_byte_string)

    @mock.patch.object(StringConverterPython2, 'convert_to_byte_string_utf8')
    def test_convert_to_string_argument_unicode_string(self, mock_convert_to_byte_string_utf8):
        mock_string = u"mock"
        mock_byte_string = b"mock"
        mock_convert_to_byte_string_utf8.return_value = mock_byte_string
        result = self.string_converter.convert_to_string(mock_string)
        self.assertEquals(result, mock_byte_string)

    @mock.patch.object(StringConverterPython2, 'convert_to_byte_string_utf8')
    def test_list_convert_to_string(self, mock_convert_to_byte_string_utf8):
        mock_list_strings = [b"mock", u"mock"]
        mock_convert_to_byte_string_utf8.side_effect = [b"mock", b"mock"]
        result = self.string_converter.list_convert_to_string(mock_list_strings)
        self.assertEquals(result, [b"mock", b"mock"])
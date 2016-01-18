
import unittest
import mock

from xcrawler.compatibility.string_converter.string_converter_python3 import StringConverterPython3


class TestStringConverterPython3(unittest.TestCase):

    def setUp(self):
        self.string_converter = StringConverterPython3()

    @mock.patch.object(StringConverterPython3, 'convert_to_unicode_string')
    def test_convert_to_string_argument_byte_string(self, mock_convert_to_unicode_string):
        mock_string = b"mock"
        mock_unicode_string = u"mock"
        mock_convert_to_unicode_string.return_value = mock_unicode_string
        result = self.string_converter.convert_to_string(mock_string)
        self.assertEquals(result, mock_unicode_string)

    @mock.patch.object(StringConverterPython3, 'convert_to_unicode_string')
    def test_convert_to_string_argument_unicode_string(self, mock_convert_to_unicode_string):
        mock_string = u"mock"
        mock_unicode_string = u"mock"
        mock_convert_to_unicode_string.return_value = mock_unicode_string
        result = self.string_converter.convert_to_string(mock_string)
        self.assertEquals(result, mock_unicode_string)

    @mock.patch.object(StringConverterPython3, 'convert_to_unicode_string')
    def test_list_convert_to_string(self, mock_convert_to_unicode_string):
        mock_list_strings = [b"mock", b"\x81", u"mock"]
        mock_convert_to_unicode_string.side_effect = [u"mock", b"\x81", u"mock"]
        result = self.string_converter.list_convert_to_string(mock_list_strings)
        self.assertEquals(result, [u"mock", b"\x81", u"mock"])


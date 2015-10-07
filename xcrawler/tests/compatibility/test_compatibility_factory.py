
import unittest
import mock

from xcrawler.compatibility.compatibility_factory import CompatibilityFactory


class TestCompatibilityFactory(unittest.TestCase):

    def setUp(self):
        self.factory = CompatibilityFactory()

    @mock.patch('xcrawler.compatibility.compatibility_factory.is_python2')
    @mock.patch('xcrawler.compatibility.compatibility_factory.FileWriteOpenerPython2')
    def test_create_file_write_strings_python2(self, mock_file_opener_write_python2, mock_is_python2):
        mock_file_opener_write = mock.Mock()
        mock_file_opener_write_python2.return_value = mock_file_opener_write
        mock_is_python2.return_value = True
        result = self.factory.create_compatible_file_opener_write()
        self.assertEquals(result, mock_file_opener_write)

    @mock.patch('xcrawler.compatibility.compatibility_factory.is_python2')
    @mock.patch('xcrawler.compatibility.compatibility_factory.FileWriteOpenerPython3')
    def test_create_file_write_strings_python3(self, mock_file_opener_write_python3, mock_is_python2):
        mock_file_opener_write = mock.Mock()
        mock_file_opener_write_python3.return_value = mock_file_opener_write
        mock_is_python2.return_value = False
        result = self.factory.create_compatible_file_opener_write()
        self.assertEquals(result, mock_file_opener_write)

    @mock.patch('xcrawler.compatibility.compatibility_factory.is_python2')
    @mock.patch('xcrawler.compatibility.compatibility_factory.ObjectConverterPython2')
    def test_create_object_converter_python2(self, mock_object_converter_python2, mock_is_python2):
        mock_converter = mock.Mock()
        mock_object_converter_python2.return_value = mock_converter
        mock_is_python2.return_value = True
        result = self.factory.create_compatible_object_converter()
        self.assertEquals(result, mock_converter)

    @mock.patch('xcrawler.compatibility.compatibility_factory.is_python2')
    @mock.patch('xcrawler.compatibility.compatibility_factory.ObjectConverterPython3')
    def test_create_object_converter_python3(self, mock_object_converter_python3, mock_is_python2):
        mock_converter = mock.Mock()
        mock_object_converter_python3.return_value = mock_converter
        mock_is_python2.return_value = False
        result = self.factory.create_compatible_object_converter()
        self.assertEquals(result, mock_converter)


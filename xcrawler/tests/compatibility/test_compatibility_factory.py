
import unittest
import mock

from xcrawler.compatibility.compatibility_factory import CompatibilityFactory


class TestCompatibilityFactory(unittest.TestCase):

    def setUp(self):
        self.factory = CompatibilityFactory()

    @mock.patch('xcrawler.compatibility.compatibility_factory.is_python2')
    @mock.patch('xcrawler.compatibility.compatibility_factory.WriteOpenerPython2')
    def test_create_file_write_strings_python2(self, mock_write_opener_python2, mock_is_python2):
        mock_write_opener = mock.Mock()
        mock_write_opener_python2.return_value = mock_write_opener
        mock_is_python2.return_value = True
        result = self.factory.create_compatible_write_opener()
        self.assertEquals(result, mock_write_opener)

    @mock.patch('xcrawler.compatibility.compatibility_factory.is_python2')
    @mock.patch('xcrawler.compatibility.compatibility_factory.WriteOpenerPython3')
    def test_create_file_write_strings_python3(self, mock_write_opener_python3, mock_is_python2):
        mock_write_opener = mock.Mock()
        mock_write_opener_python3.return_value = mock_write_opener
        mock_is_python2.return_value = False
        result = self.factory.create_compatible_write_opener()
        self.assertEquals(result, mock_write_opener)

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


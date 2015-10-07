
import unittest
import mock

from xcrawler.compatibility.compatibility_factory import CompatibilityFactory
from xcrawler.utils.info.python_info import PythonInfo


class TestCompatibilityFactory(unittest.TestCase):

    def setUp(self):
        python_info = mock.create_autospec(PythonInfo).return_value
        self.factory = CompatibilityFactory(python_info)

    @mock.patch('xcrawler.compatibility.compatibility_factory.WriteOpenerPython2')
    def test_create_file_write_strings_python2(self, mock_write_opener_python2):
        mock_write_opener = mock.Mock()
        mock_write_opener_python2.return_value = mock_write_opener
        self.factory.python_info.is_python2.return_value = True
        result = self.factory.create_compatible_write_opener()
        self.assertEquals(result, mock_write_opener)

    @mock.patch('xcrawler.compatibility.compatibility_factory.WriteOpenerPython3')
    def test_create_file_write_strings_python3(self, mock_write_opener_python3):
        mock_write_opener = mock.Mock()
        mock_write_opener_python3.return_value = mock_write_opener
        self.factory.python_info.is_python2.return_value = False
        result = self.factory.create_compatible_write_opener()
        self.assertEquals(result, mock_write_opener)

    @mock.patch('xcrawler.compatibility.compatibility_factory.ObjectConverterPython2')
    def test_create_object_converter_python2(self, mock_object_converter_python2):
        mock_converter = mock.Mock()
        mock_object_converter_python2.return_value = mock_converter
        self.factory.python_info.is_python2.return_value = True
        result = self.factory.create_compatible_object_converter()
        self.assertEquals(result, mock_converter)

    @mock.patch('xcrawler.compatibility.compatibility_factory.ObjectConverterPython3')
    def test_create_object_converter_python3(self, mock_object_converter_python3):
        mock_converter = mock.Mock()
        mock_object_converter_python3.return_value = mock_converter
        self.factory.python_info.is_python2.return_value = False
        result = self.factory.create_compatible_object_converter()
        self.assertEquals(result, mock_converter)


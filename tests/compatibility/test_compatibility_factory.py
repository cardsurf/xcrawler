
import unittest
import mock

from xcrawler.compatibility.compatibility_factory import CompatibilityFactory
from xcrawler.pythonutils.info.python_info import PythonInfo
from xcrawler.compatibility.write_opener.write_opener_python2 import WriteOpenerPython2
from xcrawler.compatibility.write_opener.write_opener_python3 import WriteOpenerPython3
from xcrawler.compatibility.object_converter.object_converter_python2 import ObjectConverterPython2
from xcrawler.compatibility.object_converter.object_converter_python3 import ObjectConverterPython3
from xcrawler.compatibility.string_converter.string_converter_python2 import StringConverterPython2
from xcrawler.compatibility.string_converter.string_converter_python3 import StringConverterPython3


class TestCompatibilityFactory(unittest.TestCase):

    def setUp(self):
        python_info = mock.create_autospec(PythonInfo).return_value
        self.factory = CompatibilityFactory(python_info)

    @mock.patch('xcrawler.compatibility.compatibility_factory.WriteOpenerPython2')
    def test_create_file_write_strings_python2(self, mock_write_opener_python2_class):
        mock_write_opener = mock.create_autospec(WriteOpenerPython2).return_value
        mock_write_opener_python2_class.return_value = mock_write_opener
        self.factory.python_info.is_python2.return_value = True
        result = self.factory.create_compatible_write_opener()
        self.assertEquals(result, mock_write_opener)

    @mock.patch('xcrawler.compatibility.compatibility_factory.WriteOpenerPython3')
    def test_create_file_write_strings_python3(self, mock_write_opener_python3_class):
        mock_write_opener = mock.create_autospec(WriteOpenerPython3).return_value
        mock_write_opener_python3_class.return_value = mock_write_opener
        self.factory.python_info.is_python2.return_value = False
        result = self.factory.create_compatible_write_opener()
        self.assertEquals(result, mock_write_opener)

    @mock.patch('xcrawler.compatibility.compatibility_factory.ObjectConverterPython2')
    def test_create_object_converter_python2(self, mock_object_converter_python2_class):
        mock_converter = mock.create_autospec(ObjectConverterPython2).return_value
        mock_object_converter_python2_class.return_value = mock_converter
        self.factory.python_info.is_python2.return_value = True
        result = self.factory.create_compatible_object_converter()
        self.assertEquals(result, mock_converter)

    @mock.patch('xcrawler.compatibility.compatibility_factory.ObjectConverterPython3')
    def test_create_object_converter_python3(self, mock_object_converter_python3_class):
        mock_converter = mock.create_autospec(ObjectConverterPython3).return_value
        mock_object_converter_python3_class.return_value = mock_converter
        self.factory.python_info.is_python2.return_value = False
        result = self.factory.create_compatible_object_converter()
        self.assertEquals(result, mock_converter)

    @mock.patch('xcrawler.compatibility.compatibility_factory.StringConverterPython2')
    def test_create_string_converter_python2(self, mock_string_converter_python2_class):
        mock_converter = mock.create_autospec(StringConverterPython2).return_value
        mock_string_converter_python2_class.return_value = mock_converter
        self.factory.python_info.is_python2.return_value = True
        result = self.factory.create_compatible_string_converter()
        self.assertEquals(result, mock_converter)

    @mock.patch('xcrawler.compatibility.compatibility_factory.StringConverterPython3')
    def test_create_string_converter_python3(self, mock_string_converter_python3_class):
        mock_converter = mock.create_autospec(StringConverterPython3).return_value
        mock_string_converter_python3_class.return_value = mock_converter
        self.factory.python_info.is_python2.return_value = False
        result = self.factory.create_compatible_string_converter()
        self.assertEquals(result, mock_converter)


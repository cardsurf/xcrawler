
import unittest
import mock

from tests.mock import mock_factory
from xcrawler.compatibility.object_converter.object_converter_python2 import ObjectConverterPython2
from xcrawler.pythonutils.converters.object_converter import StringConverter
from xcrawler.pythonutils.types.instance_resolver import InstanceResolver


class TestObjectConverterPython2(unittest.TestCase):

    def setUp(self):
        string_converter = mock.create_autospec(StringConverter).return_value
        instance_resolver = mock.create_autospec(InstanceResolver).return_value
        self.object_converter = ObjectConverterPython2(string_converter, instance_resolver)

    def test_convert_to_string_argument_object(self):
        mock_object = mock_factory.create_mock_object_with_str("mock_object")
        self.object_converter.instance_resolver.is_unicode_string.return_value = False
        result = self.object_converter.convert_to_string(mock_object)
        self.assertEquals(result, b"mock_object")

    def test_convert_to_string_argument_unicode_string(self):
        mock_object = u"mock object"
        self.object_converter.instance_resolver.is_unicode_string.return_value = True
        result = self.object_converter.convert_to_string(mock_object)
        self.assertEquals(result, u"mock object")

    @mock.patch.object(ObjectConverterPython2, 'list_convert_to_byte_string_utf8')
    def test_list_convert_to_string(self, mock_list_convert_to_byte_string_utf8):
        mock_object1 = mock_factory.create_mock_object_with_str("mock_object")
        mock_object2 = mock_factory.create_mock_object_with_str(b"mock_object")
        mock_object3 = mock_factory.create_mock_object_with_str(u"mock_object")
        list_objects = [mock_object1, mock_object2, mock_object3]
        mock_list_convert_to_byte_string_utf8.return_value = [b"mock_object", b"mock_object", b"mock_object"]
        result = self.object_converter.list_convert_to_string(list_objects)
        self.assertEquals(result, [b"mock_object", b"mock_object", b"mock_object"])

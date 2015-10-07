
import unittest
import mock

from xcrawler.tests.mock import mock_factory
from xcrawler.utils.converters.object_converter import ObjectConverter
from xcrawler.utils.converters.object_converter import StringConverter
from xcrawler.utils.types.instance_resolver import InstanceResolver


class TestObjectConverter(unittest.TestCase):

    def setUp(self):
        string_converter = mock.create_autospec(StringConverter).return_value
        instance_resolver = mock.create_autospec(InstanceResolver).return_value
        self.object_converter = ObjectConverter(string_converter, instance_resolver)

    @mock.patch.object(ObjectConverter, 'convert_to_string')
    def test_convert_to_byte_string_utf8(self, mock_convert_to_string):
        mock_object = mock.Mock()
        mock_object_string = "mock object"
        mock_object_byte_string_utf8 = b"mock object"
        mock_convert_to_string.return_value = mock_object_string
        self.object_converter.string_converter.convert_to_byte_string_utf8.return_value = mock_object_byte_string_utf8
        result = self.object_converter.convert_to_byte_string_utf8(mock_object)
        self.assertEquals(result, mock_object_byte_string_utf8)

    @mock.patch.object(ObjectConverter, 'convert_to_string')
    def test_convert_to_unicode_string(self, mock_convert_to_string):
        mock_object = mock.Mock()
        mock_object_string = "mock object"
        mock_object_unicode_string = u"mock object"
        mock_convert_to_string.return_value = mock_object_string
        self.object_converter.string_converter.convert_to_unicode_string.return_value = mock_object_unicode_string
        result = self.object_converter.convert_to_unicode_string(mock_object)
        self.assertEquals(result, mock_object_unicode_string)

    def test_convert_to_string_argument_object(self):
        mock_object = mock_factory.create_mock_object_with_str("mock_object")
        self.object_converter.instance_resolver.is_byte_string.return_value = False
        result = self.object_converter.convert_to_string(mock_object)
        self.assertEquals(result, "mock_object")

    def test_convert_to_string_argument_byte_string(self):
        mock_object = b"mock object"
        self.object_converter.instance_resolver.is_byte_string.return_value = True
        result = self.object_converter.convert_to_string(mock_object)
        self.assertEquals(result, mock_object)

    def test_convert_to_list_if_single_object_argument_single_object(self):
        mock_object = mock.Mock()
        result = self.object_converter.convert_to_list_if_single_object(mock_object)
        self.assertEquals(result, [mock_object])

    def test_convert_to_list_if_single_object_argument_list(self):
        mock_object = [mock.Mock()]
        result = self.object_converter.convert_to_list_if_single_object(mock_object)
        self.assertEquals(result, mock_object)

    @mock.patch.object(ObjectConverter, 'convert_to_byte_string_utf8')
    def test_list_convert_to_byte_string_utf8(self, mock_convert_to_byte_string_utf8):
        mock_object1 = mock_factory.create_mock_object_with_str("mock_object")
        mock_object2 = mock_factory.create_mock_object_with_str(b"mock_object")
        mock_object3 = mock_factory.create_mock_object_with_str(u"mock_object")
        list_objects = [mock_object1, mock_object2, mock_object3]
        mock_convert_to_byte_string_utf8.return_value = b"mock_object"
        result = self.object_converter.list_convert_to_byte_string_utf8(list_objects)
        self.assertEquals(result, [b"mock_object", b"mock_object", b"mock_object"])

    @mock.patch.object(ObjectConverter, 'convert_to_unicode_string')
    def test_list_convert_to_unicode_string(self, mock_convert_to_unicode_string):
        mock_object1 = mock_factory.create_mock_object_with_str("mock_object")
        mock_object2 = mock_factory.create_mock_object_with_str(b"mock_object")
        mock_object3 = mock_factory.create_mock_object_with_str(u"mock_object")
        list_objects = [mock_object1, mock_object2, mock_object3]
        mock_convert_to_unicode_string.return_value = u"mock_object"
        result = self.object_converter.list_convert_to_unicode_string(list_objects)
        self.assertEquals(result, [u"mock_object", u"mock_object", u"mock_object"])

    @mock.patch.object(ObjectConverter, 'convert_to_string')
    def test_list_convert_to_unicode_string(self, mock_convert_to_string):
        mock_object1 = mock_factory.create_mock_object_with_str("mock_object")
        mock_object2 = mock_factory.create_mock_object_with_str(b"mock_object")
        mock_object3 = mock_factory.create_mock_object_with_str(u"mock_object")
        list_objects = [mock_object1, mock_object2, mock_object3]
        mock_convert_to_string.return_value = "mock_object"
        result = self.object_converter.list_convert_to_string(list_objects)
        self.assertEquals(result, ["mock_object", "mock_object", "mock_object"])
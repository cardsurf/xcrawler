
import unittest
import mock

from xcrawler.pythonutils.types.instance_resolver import InstanceResolver


class TestInstanceResolver(unittest.TestCase):

    def setUp(self):
        self.type_resolver = InstanceResolver()

    def test_is_unicode_or_byte_string_argument_non_string(self):
        mock_object = mock.Mock()
        result = self.type_resolver.is_unicode_or_byte_string(mock_object)
        self.assertEquals(result, False)

    def test_is_unicode_or_byte_string_argument_string(self):
        mock_object = b"mock"
        result = self.type_resolver.is_unicode_or_byte_string(mock_object)
        self.assertEquals(result, True)

    def test_is_unicode_string_argument_non_unicode_string(self):
        mock_object = mock.Mock()
        result = self.type_resolver.is_unicode_string(mock_object)
        self.assertEquals(result, False)

    def test_is_unicode_string_argument_unicode_string(self):
        mock_object = u"mock"
        result = self.type_resolver.is_unicode_string(mock_object)
        self.assertEquals(result, True)

    def test_is_byte_string_argument_non_byte_string(self):
        mock_object = mock.Mock()
        result = self.type_resolver.is_byte_string(mock_object)
        self.assertEquals(result, False)

    def test_is_byte_string_argument_byte_string(self):
        mock_object = b"mock"
        result = self.type_resolver.is_byte_string(mock_object)
        self.assertEquals(result, True)

    def test_is_string_python_version_argument_non_string(self):
        mock_object = mock.Mock()
        result = self.type_resolver.is_string_python_version(mock_object)
        self.assertEquals(result, False)

    def test_is_string_python_version_argument_string(self):
        mock_object = "mock"
        result = self.type_resolver.is_string_python_version(mock_object)
        self.assertEquals(result, True)


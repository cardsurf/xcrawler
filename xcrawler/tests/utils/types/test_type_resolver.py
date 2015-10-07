
import unittest
import mock

from xcrawler.utils.types.type_resolver import TypeResolver


class TestStringConverter(unittest.TestCase):

    def setUp(self):
        self.type_resolver = TypeResolver()

    def test_is_string_argument_non_string(self):
        mock_object = mock.Mock()
        result = self.type_resolver.is_string(mock_object)
        self.assertEquals(result, False)

    def test_is_string_argument_string(self):
        mock_object = "mock"
        result = self.type_resolver.is_string(mock_object)
        self.assertEquals(result, True)

    def test_is_byte_string_argument_non_byte_string(self):
        mock_object = mock.Mock()
        result = self.type_resolver.is_byte_string(mock_object)
        self.assertEquals(result, False)

    def test_is_byte_string_argument_byte_string(self):
        mock_object = b"mock"
        result = self.type_resolver.is_byte_string(mock_object)
        self.assertEquals(result, True)

    def test_is_unicode_string_argument_non_unicode_string(self):
        mock_object = mock.Mock()
        result = self.type_resolver.is_unicode_string(mock_object)
        self.assertEquals(result, False)

    def test_is_unicode_string_argument_unicode_string(self):
        mock_object = u"mock"
        result = self.type_resolver.is_unicode_string(mock_object)
        self.assertEquals(result, True)



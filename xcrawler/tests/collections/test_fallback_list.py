
import unittest

from xcrawler.collections.fallback_list import FallbackList


class TestFallbackList(unittest.TestCase):

    def setUp(self):
        self.list_strings = ["Element 1", "Element 2", "Element 3"]
        self.fallback_list = FallbackList(self.list_strings)
        self.numbers = 10

    def test_get_valid_index(self):
        index = 0
        fallback = "FallbackValue"
        string = self.list_strings[0]
        result = self.fallback_list.get(index, fallback)
        self.assertEquals(result, string)

    def test_get_invalid_index(self):
        index = len(self.fallback_list) + 1
        fallback = "FallbackValue"
        result = self.fallback_list.get(index, fallback)
        self.assertEquals(result, fallback)


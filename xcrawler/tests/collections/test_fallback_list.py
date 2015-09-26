
import unittest

import xcrawler


class TestFallbackList(unittest.TestCase):

    def setUp(self):
        self.list_strings = ["Element 1", "Element 2", "Element 3"]
        self.fallback_list = xcrawler.FallbackList(self.list_strings)
        self.numbers = 10

    def test_get_valid_index(self):
        index = 0
        default_value = None
        string = self.list_strings[0]
        result = self.fallback_list.get(index, default_value)
        self.assertEquals(result, string)

    def test_get_invalid_index(self):
        index = len(self.fallback_list) + 1
        default_value = None
        result = self.fallback_list.get(index, default_value)
        self.assertEquals(result, default_value)


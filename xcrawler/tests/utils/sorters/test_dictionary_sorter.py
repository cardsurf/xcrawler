
import unittest

from xcrawler.utils.sorters.dictionary_sorter import DictionarySorter


class TestDictionarySorter(unittest.TestCase):

    def setUp(self):
        self.dictionary_sorter = DictionarySorter()

    def get_list_of_keys_sorted_by_name(self):
        mock_dictionary = {"width": 800, "height": 600, "title": "mock title"}
        result = self.dictionary_sorter.get_list_of_values_sorted_by_keys(mock_dictionary)
        self.assertEquals(result, ["height", "mock title", "width"])

    def test_get_list_of_values_sorted_by_keys(self):
        mock_dictionary = {"width": 800, "height": 600, "title": "mock title"}
        result = self.dictionary_sorter.get_list_of_values_sorted_by_keys(mock_dictionary)
        self.assertEquals(result, [600, "mock title", 800])




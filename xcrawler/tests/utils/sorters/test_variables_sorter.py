
import unittest
import mock

from xcrawler.utils.sorters.dictionary_sorter import DictionarySorter
from xcrawler.utils.sorters.variables_sorter import VariablesSorter


class TestVariablesSorter(unittest.TestCase):

    def setUp(self):
        dictionary_sorter = mock.create_autospec(DictionarySorter).return_value
        self.variables_sorter = VariablesSorter(dictionary_sorter)

    def test_get_list_of_variable_names_sorted_by_name(self):
        mock_object = mock.Mock()
        mock_object.__dict__ = {"width": 800, "height": 600, "title": "mock title"}
        result = self.variables_sorter.get_list_of_variable_names_sorted_by_name(mock_object)
        self.assertEquals(result, ["height", "title", "width"])

    def get_list_of_variable_values_sorted_by_name(self):
        mock_object = mock.Mock()
        mock_object.__dict__ = {"width": 800, "height": 600, "title": "mock title"}
        self.variables_sorter.dictionary_sorter.get_list_of_values_sorted_by_keys = [600, "mock title", 800]
        result = self.variables_sorter.get_list_of_variable_names_sorted_by_name(mock_object)
        self.assertEquals(result, [600, "mock title", 800])

from xcrawler.pythonutils.sorters.dictionary_sorter import DictionarySorter


class VariablesSorter(object):
    """Sorts variable names and values of an object.

    """
    def __init__(self, dictionary_sorter=DictionarySorter()):
        self.dictionary_sorter = dictionary_sorter

    def get_list_of_variable_names_sorted_by_name(self, o):
        variables = vars(o)
        names = self.dictionary_sorter.get_list_of_keys_sorted_by_name(variables)
        return names

    def get_list_of_variable_values_sorted_by_name(self, o):
        variables = vars(o)
        values = self.dictionary_sorter.get_list_of_values_sorted_by_keys(variables)
        return values


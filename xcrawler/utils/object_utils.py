

from xcrawler.utils import dict_utils


def get_list_of_variable_names_sorted_by_name(o):
    variables = vars(o)
    names = variables.keys()
    names = sorted(names)
    return names


def get_list_of_variable_values_sorted_by_name(o):
    variables = vars(o)
    values = dict_utils.get_list_of_values_sorted_by_keys(variables)
    return values




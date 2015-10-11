

class DictionarySorter:
    """Sorts keys and values of a dictionary.

    """
    def __init__(self):
        pass

    def get_list_of_keys_sorted_by_name(self, dictionary):
        keys = dictionary.keys()
        keys = sorted(keys)
        return keys

    def get_list_of_values_sorted_by_keys(self, dictionary):
        values = []
        for key in sorted(dictionary):
            values.append(dictionary[key])

        return values



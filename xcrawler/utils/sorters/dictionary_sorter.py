

class DictionarySorter:
    """Sorts keys and values o a dictionary.

    """
    def __init__(self):
        pass

    def get_list_of_values_sorted_by_keys(self, dictionary):
        values = []
        for key in sorted(dictionary):
            values.append(dictionary[key])

        return values



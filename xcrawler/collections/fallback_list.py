
class FallbackList(list):
    """A list with methods that return a default value when an exception occurs.

    """

    def get(self, index, default_value="None"):
        try:
            result = self[index]
        except IndexError:
            result = default_value
        return result


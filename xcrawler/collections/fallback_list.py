
class FallbackList(list):
    """A list with methods that return a fallback value when an exception occurs.

    """

    def get(self, index, fallback="None"):
        try:
            result = self[index]
        except IndexError:
            result = fallback
        return result


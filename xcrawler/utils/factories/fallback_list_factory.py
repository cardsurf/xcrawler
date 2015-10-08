
from xcrawler.collections.fallback_list import FallbackList


class FallbackListFactory:
    """Creates an instance of the FallbackList class.

    """

    def __init__(self):
        pass

    def create_fallback_list(self, list_object):
        fallback_list = FallbackList(list_object)
        return fallback_list



from lxml.etree import Element


class ElementFactory(object):
    """Creates an instance of the Element class.

    """
    def __init__(self):
        pass

    def create_element(self, tag):
        element = Element(tag)
        return element

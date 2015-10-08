
from lxml import etree
from lxml.cssselect import CSSSelector

from xcrawler.utils.converters.string_converter import StringConverter
from xcrawler.collections.fallback_list import FallbackList


class SelectorCss:
    """Gets a list of Elements that match a CSS selector from an instance of an Element object.

    Attributes:
        selector (CSSSelector): gets a list of Elements from an Element object.
        string_converter(StringConverter): the StringConverter that converts a string to an unicode string.
    """

    def __init__(self,
                 selector=None,
                 string_converter=StringConverter()):
        self.selector = selector
        self.string_converter = string_converter




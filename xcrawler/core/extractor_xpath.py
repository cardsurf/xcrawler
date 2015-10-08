
from xcrawler.utils.converters.string_converter import StringConverter
from xcrawler.utils.factories.fallback_list_factory import FallbackListFactory


class ExtractorXPath:
    """Extracts data from an instance of an Element object with XPath expressions.

    Attributes:
        root_element (Element): an instance of an Element object that contains nested elements.
        fallbacklist_factory (FallbackListFactory): creates an instance of the FallbackList class.
        string_converter(StringConverter): the StringConverter that converts a string to an unicode string.
    """

    def __init__(self,
                 root_element=None,
                 fallbacklist_factory=FallbackListFactory(),
                 string_converter=StringConverter()):
        self.root_element = root_element
        self.fallbacklist_factory = fallbacklist_factory
        self.string_converter = string_converter

    def xpath(self, path):
        """
        :param path: the XPath expression.
        :returns: a FallbackList of Element objects that match the XPath expression.
        """
        path = self.string_converter.convert_to_unicode_string(path)
        result = self.root_element.xpath(path)
        result = self.fallbacklist_factory.create_fallback_list(result)
        return result
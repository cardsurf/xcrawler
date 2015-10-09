
from xcrawler.utils.converters.string_converter import StringConverter
from xcrawler.utils.factories.collection_factory import CollectionFactory


class ExtractorXPath:
    """Extracts data from an instance of an Element object with XPath expressions.

    Attributes:
        root_element (Element): an instance of an Element object that contains nested elements.
        collection_factory (CollectionFactory): creates a collection of the specified type.
        string_converter(StringConverter): converts a string to an unicode string.
    """

    def __init__(self,
                 root_element=None,
                 collection_factory=CollectionFactory(),
                 string_converter=StringConverter()):
        self.root_element = root_element
        self.collection_factory = collection_factory
        self.string_converter = string_converter

    def xpath(self, path):
        """
        :param path: the XPath expression.
        :returns: a FallbackList of Element objects that match the XPath expression.
        """
        path = self.string_converter.convert_to_unicode_string(path)
        result = self.root_element.xpath(path)
        result = self.collection_factory.create_fallback_list(result)
        return result
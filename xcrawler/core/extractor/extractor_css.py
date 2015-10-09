from lxml import etree

from xcrawler.utils.converters.string_converter import StringConverter
from xcrawler.core.extractor.css_selector import CSSSelectorFactory
from xcrawler.collections.collection_factory import CollectionFactory


class ExtractorCss:
    """Extracts data from an instance of an Element object with CSS selectors.

    Attributes:
        root_element (Element): an instance of an Element object that contains nested elements.
        cssselector_factory (CSSSelectorFactory): creates an instance of the CSSSelector class.
        collection_factory (CollectionFactory): creates a collection of the specified type.
        string_converter(StringConverter): converts a string to an unicode string.
    """

    def __init__(self,
                 root_element=None,
                 cssselector_factory=CSSSelectorFactory(),
                 collection_factory=CollectionFactory(),
                 string_converter=StringConverter()):
        self.root_element = root_element
        self.cssselector_factory = cssselector_factory
        self.collection_factory = collection_factory
        self.string_converter = string_converter

    def css(self, path):
        """
        :param path: the CSS selector.
        :returns: a FallbackList of Element objects that match the CSS selector.
        """
        path = self.string_converter.convert_to_unicode_string(path)
        css_selector = self.cssselector_factory.create_css_selector(path)
        result = css_selector.__call__(self.root_element)
        result = self.collection_factory.create_fallback_list(result)
        return result

    def css_text(self, path):
        """
        :param path: the CSS selector.
        :returns: a FallbackList containing text of Element objects that match the CSS selector.
        """
        result = self.css(path)
        result = self.convert_elements_to_text(result)
        return result

    def convert_elements_to_text(self, list_elements):
        for i, element in enumerate(list_elements):
            list_elements[i] = etree.tostring(element, method="text", encoding="UTF-8")
        return list_elements

    def css_attr(self, path, attribute_name):
        """
        :param path: the CSS selector.
        :param attribute_name: the attribute name of Element objects.
        :returns: a FallbackList containing attribute values of Element objects that match the CSS selector.
        """
        result = self.css(path)
        result = self.convert_elements_to_attribute(result, attribute_name)
        return result

    def convert_elements_to_attribute(self, list_elements, attribute_name):
        for i, element in enumerate(list_elements):
            list_elements[i] = element.attrib[attribute_name]
        return list_elements



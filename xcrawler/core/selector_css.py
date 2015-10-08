
from lxml import etree

from xcrawler.utils.converters.string_converter import StringConverter
from xcrawler.utils.factories.css_selector_factory import CSSSelectorFactory
from xcrawler.utils.factories.fallback_list_factory import FallbackListFactory


class SelectorCss:
    """Gets a list of Elements that match a CSS selector from an instance of an Element object.

    Attributes:
        element (Element): an instance of an Element object that contains nested Elements.
        cssselector_factory (CSSSelectorFactory): creates an instance of the CSSSelector class.
        fallbacklist_factory (FallbackListFactory): creates an instance of the FallbackList class.
        string_converter(StringConverter): the StringConverter that converts a string to an unicode string.
    """

    def __init__(self,
                 element=None,
                 cssselector_factory=CSSSelectorFactory(),
                 fallbacklist_factory=FallbackListFactory(),
                 string_converter=StringConverter()):
        self.element = element
        self.cssselector_factory = cssselector_factory
        self.fallbacklist_factory = fallbacklist_factory
        self.string_converter = string_converter

    def css(self, path):
        """
        :param path: the CSS selector.
        :returns: a FallbackList of web page elements that match the CSS selector.
        """
        path = self.string_converter.convert_to_unicode_string(path)
        css_selector = self.cssselector_factory.create_css_selector(path)
        result = css_selector.__call__(self.element)
        result = self.fallbacklist_factory.create_fallback_list(result)
        return result

    def css_text(self, path):
        """
        :param path: the CSS selector.
        :returns: a FallbackList containing text of web page elements that match the CSS selector.
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
        :param attribute_name: the attribute name of a web page element.
        :returns: a FallbackList containing attribute values of web page elements that match the CSS selector.
        """
        result = self.css(path)
        result = self.convert_elements_to_attribute(result, attribute_name)
        return result

    def convert_elements_to_attribute(self, list_elements, attribute_name):
        for i, element in enumerate(list_elements):
            list_elements[i] = element.attrib[attribute_name]
        return list_elements



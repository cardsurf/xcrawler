
import unittest
import mock
from lxml.etree import Element
from lxml.cssselect import CSSSelector

from xcrawler.core.selector_css import SelectorCss
from xcrawler.utils.converters.string_converter import StringConverter


class TestSelectorCss(unittest.TestCase):

    def setUp(self):
        element = mock.create_autospec(Element).return_value
        selector = mock.create_autospec(CSSSelector).return_value
        self.selector_css = SelectorCss(element, selector)



import unittest
import mock
from lxml.etree import Element

from xcrawler.core.selector_css import SelectorCss
from xcrawler.utils.factories.css_selector_factory import CSSSelectorFactory
from xcrawler.utils.factories.fallback_list_factory import FallbackListFactory
from xcrawler.utils.converters.string_converter import StringConverter


class TestSelectorCss(unittest.TestCase):

    def setUp(self):
        element = mock.create_autospec(Element).return_value
        cssselector_factory = mock.create_autospec(CSSSelectorFactory).return_value
        fallbacklist_factory = mock.create_autospec(FallbackListFactory).return_value
        string_converter = mock.create_autospec(StringConverter).return_value
        self.selector_css = SelectorCss(element, cssselector_factory, fallbacklist_factory, string_converter)


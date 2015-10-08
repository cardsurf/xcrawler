
import unittest
import mock
from lxml.etree import Element

from xcrawler.core.selector_css import SelectorCss
from xcrawler.utils.converters.string_converter import StringConverter


class TestSelectorCss(unittest.TestCase):

    def setUp(self):
        element = mock.create_autospec(Element).return_value
        string_converter = mock.create_autospec(StringConverter).return_value
        self.selector_css = SelectorCss(element, string_converter)


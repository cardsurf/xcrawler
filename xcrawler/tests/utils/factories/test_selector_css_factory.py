
import unittest
import mock
from lxml.etree import Element
from lxml.cssselect import CSSSelector

from xcrawler.utils.factories.selector_css_factory import SelectorCssFactory


class TestSelectorCssFactory(unittest.TestCase):

    def setUp(self):
        self.selector_css_factory = SelectorCssFactory()

    @mock.patch('xcrawler.utils.factories.selector_css_factory.CSSSelector')
    @mock.patch('xcrawler.utils.factories.selector_css_factory.SelectorCss')
    def test_create_selector_css(self, mock_selector_css_class, mock_selector_class):
        element = mock.create_autospec(Element).return_value
        mock_selector_instance = mock.Mock()
        mock_selector_class.return_value = mock_selector_instance
        self.selector_css_factory.create_selector_css(element)
        mock_selector_css_class.assert_called_once_with(mock_selector_instance)

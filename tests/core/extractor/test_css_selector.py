import unittest

import mock

from xcrawler.core.extractor.css_selector import CSSSelectorFactory


class TestCSSSelectorFactory(unittest.TestCase):

    def setUp(self):
        self.css_selector_factory = CSSSelectorFactory()

    @mock.patch('xcrawler.core.extractor.css_selector.CSSSelector')
    def test_create_selector_css(self, mock_css_selector_class):
        mock_path = ".sidebar-blue h3 a"
        mock_selector_instance = mock.Mock()
        mock_css_selector_class.return_value = mock_selector_instance
        self.css_selector_factory.create_css_selector(mock_path)
        mock_css_selector_class.assert_called_once_with(mock_path)



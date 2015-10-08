

import unittest
import mock

from xcrawler.utils.factories.fallback_list_factory import FallbackListFactory


class TestFallbackListFactory(unittest.TestCase):

    def setUp(self):
        self.fallback_list_factory = FallbackListFactory()

    @mock.patch('xcrawler.utils.factories.fallback_list_factory.FallbackList')
    def test_create_selector_css(self, mock_fallback_list_class):
        mock_list = ["mock1", "mock2", "mock3"]
        mock_fallback_list_instance = mock.Mock()
        mock_fallback_list_class.return_value = mock_fallback_list_instance
        self.fallback_list_factory.create_fallback_list(mock_list)
        mock_fallback_list_class.assert_called_once_with(mock_list)


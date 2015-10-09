

import unittest
import mock

from xcrawler.utils.factories.collection_factory import CollectionFactory


class TestCollectionFactory(unittest.TestCase):

    def setUp(self):
        self.collection_factory = CollectionFactory()

    @mock.patch('xcrawler.utils.factories.collection_factory.FallbackList')
    def test_create_selector_css(self, mock_fallback_list_class):
        mock_list = ["mock1", "mock2", "mock3"]
        mock_fallback_list_instance = mock.Mock()
        mock_fallback_list_class.return_value = mock_fallback_list_instance
        self.collection_factory.create_fallback_list(mock_list)
        mock_fallback_list_class.assert_called_once_with(mock_list)


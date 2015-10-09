
import unittest
import mock
try:
    import Queue as queue
except ImportError:
    import queue

from xcrawler.threads.thread_factory import ThreadFactory
from xcrawler.threads.page_processor import PageProcessor
from xcrawler.threads.item_processor import ItemProcessor
from xcrawler.core.config import Config

class TestThreadFactory(unittest.TestCase):

    def setUp(self):
        self.thread_factory = ThreadFactory()

    @mock.patch('xcrawler.threads.thread_factory.PageProcessor')
    def test_create_page_processor(self, mock_page_processor_class):
        mock_config = mock.create_autospec(Config).return_value
        mock_page_queue = mock.create_autospec(queue).return_value
        mock_item_queue = mock.create_autospec(queue).return_value
        mock_page_processor = mock.create_autospec(PageProcessor).return_value
        mock_page_processor_class.return_value = mock_page_processor
        result = self.thread_factory.create_page_processor(mock_config, mock_page_queue, mock_item_queue)
        self.assertEquals(result, mock_page_processor)

    @mock.patch('xcrawler.threads.thread_factory.ItemProcessor')
    def test_create_page_processor(self, mock_item_processor_class):
        mock_config = mock.create_autospec(Config).return_value
        mock_item_queue = mock.create_autospec(queue).return_value
        mock_item_processor = mock.create_autospec(ItemProcessor).return_value
        mock_item_processor_class.return_value = mock_item_processor
        result = self.thread_factory.create_item_processor(mock_config, mock_item_queue)
        self.assertEquals(result, mock_item_processor)

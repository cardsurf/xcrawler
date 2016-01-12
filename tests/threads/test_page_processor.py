
import unittest
import mock
try:
    import Queue as queue
except ImportError:
    import queue

from tests.mock import mock_factory
from xcrawler.threads.page_processor import PageProcessor
from xcrawler.http.requests.request_sender import RequestSender


class TestPageProcessor(unittest.TestCase):
    
    def setUp(self):
        mock_config = mock_factory.create_mock_config()
        mock_page_queue = mock.create_autospec(queue).return_value
        mock_item_queue = mock.create_autospec(queue).return_value
        request_sender = mock.create_autospec(RequestSender).return_value
        self.page_processor = PageProcessor(mock_config, mock_page_queue, mock_item_queue, request_sender)
        
    @mock.patch('xcrawler.threads.page_processor.time.sleep')
    def test_wait_to_fetch_page(self, mock_time_function):
        self.page_processor.config.fetch_delay = 0.5
        self.page_processor.wait_to_fetch_page()
        mock_time_function.assert_called_once_with(self.page_processor.config.fetch_delay)
   
    @mock.patch.object(PageProcessor, 'put_extracted_items_in_queue')
    @mock.patch.object(PageProcessor, 'put_extracted_pages_in_queue')
    def test_process_page(self, mock_put_extracted_pages_in_queue, mock_put_extracted_items_in_queue):
        self.page_processor.request_sender.get_element.return_value = "<html><br>Page title</br></html>"
        mock_page = mock_factory.create_mock_page()
        mock_page.url = "http://test.com/link/to/example_page.html"
        self.page_processor.process_page(mock_page)
        self.assertEquals(mock_page.content, "<html><br>Page title</br></html>")
        mock_put_extracted_pages_in_queue.assert_called_once_with(mock_page)
        mock_put_extracted_items_in_queue.assert_called_once_with(mock_page)

    def test_put_extracted_pages_in_queue(self):
        mock_page = mock_factory.create_mock_page()
        mock_extracted_pages = [mock.Mock()] * 10
        mock_page.extract_pages.return_value = mock_extracted_pages
        self.page_processor.put_extracted_pages_in_queue(mock_page)
        self.assertEquals(self.page_processor.page_queue.put.call_count, len(mock_extracted_pages))
        
    def test_put_extracted_items_in_queue(self):
        mock_page = mock_factory.create_mock_page()
        mock_extracted_items = [mock.Mock()] * 10
        mock_page.extract_items.return_value = mock_extracted_items
        self.page_processor.put_extracted_items_in_queue(mock_page)
        self.assertEquals(self.page_processor.items_queue.put.call_count, len(mock_extracted_items))


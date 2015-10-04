
import unittest
import mock
try:
    import Queue as queue
    import __builtin__ as builtins
except ImportError:
    import queue
    import builtins

import xcrawler
from xcrawler.tests.mock import mock_factory


class TestPageProcessor(unittest.TestCase):
    
    def setUp(self):
        mock_config = mock_factory.create_mock_config()
        mock_page_queue = mock.create_autospec(queue).return_value
        mock_item_queue = mock.create_autospec(queue).return_value
        self.page_processor = xcrawler.PageProcessor(mock_config, mock_page_queue, mock_item_queue)
        
    @mock.patch('xcrawler.threads.page_processor.time.sleep') 
    def test_wait_to_fetch_page(self, mock_time_function):
        self.page_processor.config.fetch_delay = 0.5
        self.page_processor.wait_to_fetch_page()
        mock_time_function.assert_called_once_with(self.page_processor.config.fetch_delay)
   
    @mock.patch.object(xcrawler.PageProcessor, 'put_extracted_items_in_queue') 
    @mock.patch.object(xcrawler.PageProcessor, 'put_extracted_pages_in_queue')
    @mock.patch.object(xcrawler.PageProcessor, 'fetch_content') 
    def test_process_page(self, mock_fetch_content,
                          mock_put_extracted_pages_in_queue, mock_put_extracted_items_in_queue):
        mock_fetch_content.return_value = "<html><br>Page title</br></html>"
        mock_page = mock.Mock()
        self.page_processor.process_page(mock_page)
        self.assertEquals(mock_page.content, mock_fetch_content.return_value)
        mock_fetch_content.assert_called_once_with(mock_page)
        mock_put_extracted_pages_in_queue.assert_called_once_with(mock_page)
        mock_put_extracted_items_in_queue.assert_called_once_with(mock_page)      

    @mock.patch('xcrawler.threads.page_processor.Request')
    @mock.patch('xcrawler.threads.page_processor.urlopen')
    @mock.patch('xcrawler.threads.page_processor.etree')
    def test_fetch_content(self, mock_etree_module, mock_urlopen_function,  mock_request_class):
        mock_page = mock.Mock()
        mock_page.url = "http://mockurl.mock"
        mock_etree_module.HTML.return_value = "<html><br>Page title</br></html>"
        mock_page.content = self.page_processor.fetch_content(mock_page)
        self.assertEquals(mock_page.content, mock_etree_module.HTML.return_value)

    @mock.patch('xcrawler.tests.threads.test_page_processor.builtins.print')
    def test_handle_url_error_exception(self, mock_print_function):
        mock_page = mock.Mock()
        mock_page.url = "http://mockurl.mock"
        mock_exception = mock.Mock()
        mock_exception.reason = "BadStatusLine"
        self.page_processor.handle_url_error_exception(mock_page, mock_exception)
        self.assertEquals(mock_print_function.call_count, 2)
     
    @mock.patch('xcrawler.tests.threads.test_page_processor.builtins.print')
    def test_handle_bad_status_line_exception(self, mock_print_function):
        mock_page = mock.Mock()
        mock_page.url = "http://mockurl.mock"
        mock_exception = mock.Mock()
        mock_exception.message = "404: not found"
        self.page_processor.handle_bad_status_line_exception(mock_page, mock_exception)
        self.assertEquals(mock_print_function.call_count, 2)
        
    @mock.patch('xcrawler.tests.threads.test_page_processor.builtins.print')
    def test_handle_socket_timeout_exception(self, mock_print_function):
        mock_page = mock.Mock()
        mock_page.url = "http://mockurl.mock"
        mock_exception = mock.Mock()
        mock_exception.message = "socket timeout"
        self.page_processor.handle_socket_timeout_exception(mock_page, mock_exception)
        self.assertEquals(mock_print_function.call_count, 2)

    @mock.patch('xcrawler.tests.threads.test_page_processor.builtins.print')
    def test_handle_base_exception(self, mock_print_function):
        mock_page = mock.Mock()
        mock_page.url = "http://mockurl.mock"
        mock_exception = mock.Mock()
        mock_exception.message = "Base exception message"
        self.page_processor.handle_base_exception(mock_page, mock_exception)
        self.assertEquals(mock_print_function.call_count, 2)

    def test_put_extracted_pages_in_queue(self):
        mock_page = mock.Mock()
        mock_extracted_pages = [mock.Mock()] * 10
        mock_page.extract_pages.return_value = mock_extracted_pages
        self.page_processor.put_extracted_pages_in_queue(mock_page)
        self.assertEquals(self.page_processor.page_queue.put.call_count, len(mock_extracted_pages))
        
    def test_put_extracted_items_in_queue(self):
        mock_page = mock.Mock()
        mock_extracted_items = [mock.Mock()] * 10
        mock_page.extract_items.return_value = mock_extracted_items
        self.page_processor.put_extracted_items_in_queue(mock_page)
        self.assertEquals(self.page_processor.items_queue.put.call_count, len(mock_extracted_items))


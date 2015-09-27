
import unittest
import mock
import Queue

import xcrawler
from xcrawler.tests.mock import mock_factory


class TestWorkExecutor(unittest.TestCase):
    
    def setUp(self):
        mock_config = mock_factory.create_mock_config()
        self.work_executor = xcrawler.WorkExecutor(mock_config)
        self.work_executor.page_queue = mock.create_autospec(Queue).return_value
        self.work_executor.item_queue = mock.create_autospec(Queue).return_value
        self.work_executor.item_processor = mock.create_autospec(xcrawler.ItemProcessor).return_value
          
    @mock.patch('xcrawler.threads.work_executor.PageProcessor') 
    def test_spawn_page_queue_threads(self, page_processor_class):
        page_processor = page_processor_class.return_value
        self.work_executor.spawn_page_queue_threads()
        self.assertEquals(page_processor.start.call_count, self.work_executor.config.number_of_threads)
        
    @mock.patch('xcrawler.threads.work_executor.ItemProcessor') 
    def test_spawn_item_queue_thread(self, item_processor_class):
        item_processor = item_processor_class.return_value
        self.work_executor.spawn_item_queue_thread()
        self.assertEquals(item_processor.start.call_count, 1)
                
    @mock.patch('xcrawler.threads.work_executor.Page')   
    def test_add_pages_to_queue(self, page_class):
        mock_crawler = mock_factory.create_mock_crawler()
        self.work_executor.add_pages_to_queue(mock_crawler)
        self.assertEquals(self.work_executor.page_queue.put.call_count, len(mock_crawler.start_urls))

    def test_wait_until_work_is_done(self):
        self.work_executor.wait_until_work_is_done()
        self.assertEquals(self.work_executor.page_queue.join.call_count, 1)
        self.assertEquals(self.work_executor.item_queue.join.call_count, 1)
                   
    @mock.patch.object(xcrawler.WorkExecutor, 'add_pages_to_queue')
    @mock.patch.object(xcrawler.WorkExecutor, 'wait_until_work_is_done')   
    def test_execute_work(self, mock_wait_until_work_is_done, mock_add_pages_to_queue):
        mock_crawler = mock_factory.create_mock_crawler()
        self.work_executor.execute_work(mock_crawler)
        self.assertEquals(self.work_executor.item_processor.open_output_file_if_needed.call_count, 1)
        self.assertEquals(mock_add_pages_to_queue.call_count, 1)
        self.assertEquals(mock_wait_until_work_is_done.call_count, 1)
        self.assertEquals(self.work_executor.item_processor.close_output_file_if_needed.call_count, 1)                  
        


import unittest
import mock
try:
    import Queue as queue
except ImportError:
    import queue

from xcrawler.tests.mock import mock_factory
from xcrawler.threads.work_executor import WorkExecutor
from xcrawler.threads.page_processor import PageProcessor
from xcrawler.threads.item_processor import ItemProcessor
from xcrawler.threads.thread_factory import ThreadFactory


class TestWorkExecutor(unittest.TestCase):
    
    def setUp(self):
        mock_config = mock_factory.create_mock_config()
        thread_factory = mock.create_autospec(ThreadFactory).return_value
        self.work_executor = WorkExecutor(mock_config, thread_factory)
        self.work_executor.page_queue = mock.create_autospec(queue).return_value
        self.work_executor.item_queue = mock.create_autospec(queue).return_value
        self.work_executor.item_processor = mock.create_autospec(ItemProcessor).return_value
          
    def test_spawn_page_queue_threads(self):
        mock_page_processor = mock.create_autospec(PageProcessor).return_value
        self.work_executor.thread_factory.create_page_processor.return_value = mock_page_processor
        self.work_executor.spawn_page_queue_threads()
        self.assertEquals(mock_page_processor.start.call_count, self.work_executor.config.number_of_threads)
        
    def test_spawn_item_queue_thread(self):
        mock_item_processor = mock.create_autospec(ItemProcessor).return_value
        self.work_executor.thread_factory.create_item_processor.return_value = mock_item_processor
        self.work_executor.spawn_item_queue_thread()
        self.assertEquals(self.work_executor.item_processor, mock_item_processor)

    def test_add_pages_to_queue(self):
        mock_start_pages = mock_factory.create_mock_pages(10)
        self.work_executor.add_pages_to_queue(mock_start_pages)
        self.assertEquals(self.work_executor.page_queue.put.call_count, len(mock_start_pages))

    def test_wait_until_work_is_done(self):
        self.work_executor.wait_until_work_is_done()
        self.assertEquals(self.work_executor.page_queue.join.call_count, 1)
        self.assertEquals(self.work_executor.item_queue.join.call_count, 1)
                   
    @mock.patch.object(WorkExecutor, 'add_pages_to_queue')
    @mock.patch.object(WorkExecutor, 'wait_until_work_is_done')
    def test_execute_work(self, mock_wait_until_work_is_done, mock_add_pages_to_queue):
        mock_start_pages = mock_factory.create_mock_pages(10)
        self.work_executor.execute_work(mock_start_pages)
        self.assertEquals(self.work_executor.item_processor.open_output_file_if_needed.call_count, 1)
        self.assertEquals(mock_add_pages_to_queue.call_count, 1)
        self.assertEquals(mock_wait_until_work_is_done.call_count, 1)
        self.assertEquals(self.work_executor.item_processor.close_output_file_if_needed.call_count, 1)                  



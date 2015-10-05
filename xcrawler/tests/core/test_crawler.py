
import unittest
import mock

from xcrawler.tests.mock import mock_factory
from xcrawler.core.crawler import XCrawler


class TestXCrawler(unittest.TestCase):
    
    def setUp(self):
        start_pages = mock_factory.create_mock_pages(10)
        self.crawler = XCrawler(start_pages)

    @mock.patch('xcrawler.core.crawler.WorkExecutor')
    def test_run_with_empty_start_pages(self, mock_work_executor_module):
        mock_work_executor_instance = mock_work_executor_module.return_value
        self.crawler.start_pages = []
        self.crawler.run()
        self.assertFalse(mock_work_executor_instance.execute_work.called)

    @mock.patch('xcrawler.core.crawler.WorkExecutor')
    def test_run_with_non_empty_start_pages(self, mock_work_executor_module):
        mock_work_executor_instance = mock_work_executor_module.return_value
        self.crawler.start_pages = mock_factory.create_mock_pages(10)
        self.crawler.run()
        mock_work_executor_instance.execute_work.assert_called_once_with(self.crawler.start_pages)



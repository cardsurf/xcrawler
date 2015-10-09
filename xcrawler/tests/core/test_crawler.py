import unittest

import mock

from xcrawler.tests.mock import mock_factory
from xcrawler.core.crawler.crawler import XCrawler
from xcrawler.core.crawler.config import ConfigFactory
from xcrawler.threads.executors.work_executor import WorkExecutor
from xcrawler.threads.executors.executor_factory import ExecutorFactory


class TestXCrawler(unittest.TestCase):
    
    def setUp(self):
        start_pages = mock_factory.create_mock_pages(10)
        config_factory = mock.create_autospec(ConfigFactory).return_value
        executor_factory = mock.create_autospec(ExecutorFactory).return_value
        self.crawler = XCrawler(start_pages, config_factory, executor_factory)

    def test_run_argument_empty_start_pages(self):
        mock_executor = mock.create_autospec(WorkExecutor).return_value
        self.crawler.executor_factory.create_work_executor.return_value = mock_executor
        self.crawler.start_pages = []
        self.crawler.run()
        self.assertFalse(mock_executor.execute_work.called)

    def test_run_argument_non_empty_start_pages(self):
        mock_executor = mock.create_autospec(WorkExecutor).return_value
        self.crawler.executor_factory.create_work_executor.return_value = mock_executor
        self.crawler.run()
        mock_executor.execute_work.assert_called_once_with(self.crawler.start_pages)




import unittest
import mock

from xcrawler.threads.executor_factory import ExecutorFactory
from xcrawler.threads.work_executor import WorkExecutor
from xcrawler.core.config import Config


class TestExecutorFactory(unittest.TestCase):

    def setUp(self):
        self.executor_factory = ExecutorFactory()

    @mock.patch('xcrawler.threads.executor_factory.WorkExecutor')
    def test_create_work_executor(self, mock_work_executor_class):
        mock_config = mock.create_autospec(Config).return_value
        mock_work_executor = mock.create_autospec(WorkExecutor).return_value
        mock_work_executor_class.return_value = mock_work_executor
        result = self.executor_factory.create_work_executor(mock_config)
        self.assertEquals(result, mock_work_executor)

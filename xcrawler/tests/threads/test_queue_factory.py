
import unittest
import mock
try:
    import Queue as queue
except ImportError:
    import queue

from xcrawler.threads.queue_factory import QueueFactory


class TestQueueFactory(unittest.TestCase):

    def setUp(self):
        self.queue_factory = QueueFactory()

    @mock.patch('xcrawler.threads.queue_factory.queue.Queue')
    def test_create_queue(self, mock_queue_class):
        mock_queue = mock.create_autospec(queue.Queue).return_value
        mock_queue_class.return_value = mock_queue
        result = self.queue_factory.create_queue()
        self.assertEquals(result, mock_queue)

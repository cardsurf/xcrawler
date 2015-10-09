import unittest

import mock

from xcrawler.core.crawler.config import ConfigFactory


class TestConfigFactory(unittest.TestCase):

    def setUp(self):
        self.config_factory = ConfigFactory()

    @mock.patch('xcrawler.core.crawler.config.Config')
    def test_create_queue(self, mock_config_class):
        mock_config = mock.create_autospec(ConfigFactory).return_value
        mock_config_class.return_value = mock_config
        result = self.config_factory.create_config()
        self.assertEquals(result, mock_config)

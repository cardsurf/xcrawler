import unittest

import mock

from xcrawler.core.config.config_factory import ConfigFactory
from xcrawler.core.config.config import Config


class TestConfigFactory(unittest.TestCase):

    def setUp(self):
        self.config_factory = ConfigFactory()

    @mock.patch('xcrawler.core.config.config_factory.Config')
    def test_create_queue(self, mock_config_class):
        mock_config = mock.create_autospec(Config).return_value
        mock_config_class.return_value = mock_config
        result = self.config_factory.create_config()
        self.assertEquals(result, mock_config)

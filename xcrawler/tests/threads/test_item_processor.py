
import unittest
import mock
try:
    import Queue as queue
    import __builtin__ as builtins
except ImportError:
    import queue
    import builtins

from xcrawler.tests.mock import mock_factory
from xcrawler.files.writers.item_writer import ItemWriter
from xcrawler.threads.item_processor import ItemProcessor
from xcrawler.core.config import Config


class TestItemProcessor(unittest.TestCase):

    def setUp(self):
        mock_config = mock_factory.create_mock_config()
        mock_item_queue = mock.create_autospec(queue).return_value
        mock_item_writer = mock.create_autospec(ItemWriter()).return_value
        self.item_processor = ItemProcessor(mock_config, mock_item_queue)
        self.item_processor.item_writer = mock_item_writer
        self.item_processor.no_items_received = True
        
    @mock.patch('xcrawler.tests.threads.test_item_processor.builtins.print')
    def test_process_item_output_mode_print(self, mock_print_function):
        self.item_processor.config.output_mode = Config.OUTPUT_MODE_PRINT
        mock_item = mock.Mock()
        self.item_processor.process_item(mock_item)
        mock_print_function.assert_called_once_with(mock_item)
   
    def test_process_item_output_mode_file(self):
        self.item_processor.config.output_mode = Config.OUTPUT_MODE_FILE
        mock_item = mock.Mock()
        self.item_processor.process_item(mock_item)
        self.item_processor.item_writer.write_item.assert_called_once_with(mock_item)

    @mock.patch('xcrawler.threads.item_processor.ItemWriter') 
    def test_open_output_file_if_needed_is_needed(self, mock_item_writer_class):
        self.item_processor.config.output_mode = Config.OUTPUT_MODE_FILE
        self.item_processor.open_output_file_if_needed()
        self.item_processor.item_writer.open_output_file.assert_called_once_with(self.item_processor.config.output_file_name)
        
    def test_open_output_file_if_needed_not_needed(self):
        self.item_processor.config.output_mode = Config.OUTPUT_MODE_PRINT
        self.assertNotEquals(self.item_processor.config.output_mode,  Config.OUTPUT_MODE_FILE)
        
    def test_close_output_file_if_needed_is_needed(self):
        self.item_processor.config.output_mode = Config.OUTPUT_MODE_FILE
        self.item_processor.close_output_file_if_needed()
        self.item_processor.item_writer.close_output_file.assert_called_once_with()
        
    def test_close_output_file_if_needed_not_needed(self):
        self.item_processor.config.output_mode = Config.OUTPUT_MODE_PRINT
        self.assertNotEquals(self.item_processor.config.output_mode,  Config.OUTPUT_MODE_FILE)
        


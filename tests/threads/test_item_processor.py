import unittest

import mock

try:
    import Queue as queue
    import __builtin__ as builtins
except ImportError:
    import queue
    import builtins

from tests.mock import mock_factory
from xcrawler.files.writers.item_writer import ItemWriter
from xcrawler.files.writers.item_writer import ItemWriterFactory
from xcrawler.threads.item_processor import ItemProcessor
from xcrawler.core.crawler.config import Config
from xcrawler.files.filepaths.filepath_splitter import FilePathSplitter
from xcrawler.files.writers.binary_writer import BinaryWriter
from xcrawler.files.writers.object_writer_csv import ObjectWriterCsv


class TestItemProcessor(unittest.TestCase):

    def setUp(self):
        mock_config = mock_factory.create_mock_config()
        mock_item_queue = mock.create_autospec(queue).return_value
        mock_item_writer = mock.create_autospec(ItemWriter).return_value
        mock_filepath_splitter = mock.create_autospec(FilePathSplitter).return_value
        mock_binary_writer = mock.create_autospec(BinaryWriter).return_value
        self.item_processor = ItemProcessor(mock_config, mock_item_queue, mock_filepath_splitter,
                                            mock_binary_writer)
        self.item_processor.item_writer = mock_item_writer
        self.item_processor.no_items_received = True
        
    @mock.patch('tests.threads.test_item_processor.builtins.print')
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

    @mock.patch('xcrawler.threads.item_processor.ItemWriterFactory')
    def test_open_output_file_if_needed_is_needed(self, mock_item_writer_factory_class):
        mock_item_writer = mock.create_autospec(ItemWriter).return_value
        mock_writer_factory_instance =  mock.create_autospec(ItemWriterFactory).return_value
        mock_writer_factory_instance.create_item_writer_based_on_file_extension.return_value = mock_item_writer
        mock_item_writer_factory_class.return_value = mock_writer_factory_instance

        self.item_processor.config.output_mode = Config.OUTPUT_MODE_FILE
        self.item_processor.open_output_file_if_needed()
        self.assertEquals(self.item_processor.item_writer, mock_item_writer)
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

    @mock.patch.object(ItemProcessor, 'replace_placeholder_with_null_byte')
    def test_fix_csv_writer_null_byte_bug(self, mock_replace_placeholder_with_null_byte):
        self.item_processor.config.output_file_name = "mock_output_file.csv"
        self.item_processor.filepath_splitter.get_file_extension.return_value = ".csv"
        self.item_processor.fix_csv_writer_null_byte_bug()
        mock_replace_placeholder_with_null_byte.assert_called_once_with("mock_output_file.csv")

    def test_replace_placeholder_with_null_byte(self):
        mock_file_name =  "mock_output_file.csv"
        self.item_processor.replace_placeholder_with_null_byte(mock_file_name)
        self.item_processor.binary_writer.replace.assert_called_once_with(
                                    mock_file_name,
                                    ObjectWriterCsv.CSV_WRITER_NULL_BYTE_PLACEHOLDER,
                                    ObjectWriterCsv.CSV_WRITER_NULL_BYTE)


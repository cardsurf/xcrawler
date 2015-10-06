
import unittest
import mock
try:
    import __builtin__ as builtins
except ImportError:
    import builtins

from xcrawler.files.writers.item_writer import ItemWriter
from xcrawler.files.strategies.writeobject.write_object_csv import WriteObjectCsv
from xcrawler.compatibility.compatible_file_opener_write import CompatibleFileOpenerWrite


class TestItemWriter(unittest.TestCase):

    def setUp(self):
        self.item_writer = ItemWriter()
        self.item_writer.write_object_strategy = mock.create_autospec(WriteObjectCsv).return_value
        self.item_writer.file_opener = mock.create_autospec(CompatibleFileOpenerWrite).return_value
        self.item_writer._ItemWriter__no_items_written_to_file = True

    def test_write_headers(self):
        mock_item = mock.Mock()
        self.item_writer.write_headers(mock_item)
        self.item_writer.write_object_strategy.write_headers.assert_called_once_with(mock_item)
        
    @mock.patch.object(ItemWriter, 'write_headers')
    def test_write_item_first_item(self, mock_write_headers):
        self.item_writer._ItemWriter__no_items_written_to_file = True
        mock_item = mock.Mock()
        self.item_writer.write_item(mock_item)
        self.assertFalse(self.item_writer._ItemWriter__no_items_written_to_file)
        
        mock_write_headers.assert_called_once_with(mock_item)
        self.item_writer.write_object_strategy.write_item.assert_called_once_with(mock_item)
        
    def test_write_item_non_first_item(self):
        self.item_writer._ItemWriter__no_items_written_to_file = False
        mock_item = mock.Mock()
        self.item_writer.write_item(mock_item)
        self.item_writer.write_object_strategy.write_item.assert_called_once_with(mock_item)

    def test_open_output_file(self):
        mock_file_name = "mock_output.csv"
        mock_file = mock.Mock()
        self.item_writer.write_object_strategy.open_file.return_value = mock_file
        self.item_writer.open_output_file(mock_file_name)
        self.assertEquals(self.item_writer.output_file, mock_file)

    def test_close_output_file(self):
        self.item_writer.output_file = mock.Mock()
        self.item_writer.close_output_file()
        
        self.item_writer.output_file.close.assert_called_once_with()
        


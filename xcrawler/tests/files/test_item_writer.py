
import unittest
import mock

from xcrawler.files.writers.item_writer import ItemWriter
from xcrawler.files.writers.object_writer import ObjectWriter
from xcrawler.files.writers.object_writer_csv import ObjectWriterCsv
from xcrawler.files.writers.item_writer import ItemWriterFactory
from xcrawler.files.writers.writer_factory import WriterFactory
from xcrawler.utils.filepaths.filepath_splitter import FilePathSplitter


class TestItemWriter(unittest.TestCase):

    def setUp(self):
        mock_object_writer = mock.create_autospec(ObjectWriter).return_value
        self.item_writer = ItemWriter(mock_object_writer)
        self.item_writer._ItemWriter__no_items_written_to_file = True

    def test_write_headers(self):
        mock_item = mock.Mock()
        self.item_writer.write_headers(mock_item)
        self.item_writer.object_writer.write_headers.assert_called_once_with(mock_item)
        
    @mock.patch.object(ItemWriter, 'write_headers')
    def test_write_item_first_item(self, mock_write_headers):
        self.item_writer._ItemWriter__no_items_written_to_file = True
        mock_item = mock.Mock()
        self.item_writer.write_item(mock_item)
        self.assertFalse(self.item_writer._ItemWriter__no_items_written_to_file)
        
        mock_write_headers.assert_called_once_with(mock_item)
        self.item_writer.object_writer.write_object.assert_called_once_with(mock_item)
        
    def test_write_item_non_first_item(self):
        self.item_writer._ItemWriter__no_items_written_to_file = False
        mock_item = mock.Mock()
        self.item_writer.write_item(mock_item)
        self.item_writer.object_writer.write_object.assert_called_once_with(mock_item)

    def test_open_output_file(self):
        mock_file_name = "mock_output.csv"
        mock_file = mock.Mock()
        self.item_writer.object_writer.open_file.return_value = mock_file
        self.item_writer.open_output_file(mock_file_name)
        self.assertEquals(self.item_writer.output_file, mock_file)

    def test_close_output_file(self):
        self.item_writer.output_file = mock.Mock()
        self.item_writer.close_output_file()
        
        self.item_writer.output_file.close.assert_called_once_with()
        



class TestItemWriterFactory(unittest.TestCase):

    def setUp(self):
        filepath_splitter = mock.create_autospec(FilePathSplitter).return_value
        object_writer_factory = mock.create_autospec(WriterFactory).return_value
        self.item_writer_factory = ItemWriterFactory(filepath_splitter, object_writer_factory)

    @mock.patch.object(ItemWriterFactory, 'create_item_writer_csv')
    def test_create_item_writer_based_on_file_extension_csv(self, mock_create_item_writer_csv):
        mock_file_name = "mock.csv"
        self.item_writer_factory.filepath_splitter.get_file_extension.return_value = ".csv"
        mock_item_writer = mock.Mock()
        mock_create_item_writer_csv.return_value = mock_item_writer
        result = self.item_writer_factory.create_item_writer_based_on_file_extension(mock_file_name)
        self.assertEquals(result, mock_item_writer)

    def test_create_item_writer_based_on_file_extension_value_error(self):
        mock_file_name = "mock.exe"
        self.item_writer_factory.filepath_splitter.get_file_extension.return_value = ".exe"
        self.assertRaises(ValueError, self.item_writer_factory.create_item_writer_based_on_file_extension, mock_file_name)

    @mock.patch('xcrawler.files.writers.item_writer.ItemWriter')
    def test_create_item_writer_csv(self, mock_item_writer_class):
        mock_object_writer_csv = mock.create_autospec(ObjectWriterCsv).return_value
        mock_item_writer_csv = mock.create_autospec(ItemWriter).return_value
        self.item_writer_factory.object_writer_factory.create_object_writer_csv.return_value = mock_object_writer_csv
        mock_item_writer_class.return_value = mock_item_writer_csv
        result = self.item_writer_factory.create_item_writer_csv()
        self.assertEquals(result, mock_item_writer_csv)


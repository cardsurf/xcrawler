
import unittest
import mock
try:
    import __builtin__ as builtins
except ImportError:
    import builtins

from xcrawler.files.writers.item_writer import ItemWriter
from xcrawler.files.strategies.writeobject.write_object_strategy import WriteObjectStrategy
from xcrawler.files.openers.file_opener_write import FileOpenerWrite


class TestItemWriter(unittest.TestCase):

    def setUp(self):
        self.item_writer = ItemWriter()
        self.item_writer.write_object_strategy = mock.create_autospec(WriteObjectStrategy).return_value
        self.item_writer.file_opener = mock.create_autospec(FileOpenerWrite).return_value
        self.item_writer._ItemWriter__no_items_written_to_file = True

    @mock.patch('xcrawler.files.writers.item_writer.string_utils.is_string')
    def test_write_headers_to_output_file_string_argument(self, mock_is_string_function):
        mock_string = "mock"        
        mock_is_string_function.return_value = True

        self.item_writer.write_headers_to_output_file(mock_string)
        mock_is_string_function.assert_called_once_with(mock_string)
           
    @mock.patch('xcrawler.files.writers.item_writer.string_utils.is_string')
    @mock.patch('xcrawler.files.writers.item_writer.object_utils.get_list_of_variable_names_sorted_by_name')
    def test_write_headers_to_output_file_item_argument(self, mock_get_list_of_variable_names_sorted_by_name, mock_is_string_function):
        mock_item = mock.Mock()
        mock_item_variables = { "width": 800, "height": 600, "title": "mock title" }
        mock_names = ["height", "mock title", "width"]
        mock_is_string_function.return_value = False
        mock_get_list_of_variable_names_sorted_by_name.return_value = ["height", "mock title", "width"]
        self.item_writer.write_headers_to_output_file(mock_item)
        self.item_writer.write_object_strategy.write.assert_called_once_with(mock_names)
        
    @mock.patch.object(ItemWriter, 'write_headers_to_output_file')
    @mock.patch.object(ItemWriter, 'write_item_to_output_file')
    def test_write_item_first_item(self, mock_write_item_to_output_file, mock_write_headers_to_output_file):
        self.item_writer._ItemWriter__no_items_written_to_file = True
        mock_item = mock.Mock()
        self.item_writer.write_item(mock_item)
        self.assertFalse(self.item_writer._ItemWriter__no_items_written_to_file)
        
        mock_write_headers_to_output_file.assert_called_once_with(mock_item)
        mock_write_item_to_output_file.assert_called_once_with(mock_item)
        
    @mock.patch.object(ItemWriter, 'write_item_to_output_file')
    def test_write_item_non_first_item(self, mock_write_item_to_output_file):
        self.item_writer._ItemWriter__no_items_written_to_file = False
        mock_item = mock.Mock()
        self.item_writer.write_item(mock_item)
        
        mock_write_item_to_output_file.assert_called_once_with(mock_item)
        
    @mock.patch('xcrawler.files.writers.item_writer.string_utils.is_string')
    @mock.patch.object(ItemWriter, 'write_string_to_output_file')
    def test_write_item_to_output_file_string_argument(self, mock_write_string_to_output_file, mock_is_string_function):
        mock_is_string_function.return_value = True
        mock_string = "mock"
        self.item_writer.write_item_to_output_file(mock_string)
        
        mock_is_string_function.assert_called_once_with(mock_string)
        mock_write_string_to_output_file.assert_called_once_with(mock_string)
        
    @mock.patch('xcrawler.files.writers.item_writer.string_utils.is_string')
    @mock.patch.object(ItemWriter, 'write_item_variables_to_output_file')
    def test_write_item_to_output_file_item_argument(self, mock_write_item_variables_to_output_file,
                                                      mock_is_string_function):
        mock_is_string_function.return_value = False
        mock_item = mock.Mock()
        self.item_writer.write_item_to_output_file(mock_item)
        
        mock_is_string_function.assert_called_once_with(mock_item)
        mock_write_item_variables_to_output_file.assert_called_once_with(mock_item)   
        
    def test_write_string_to_output_file(self):
        mock_string = "mock"
        self.item_writer.write_string_to_output_file(mock_string)
        self.item_writer.write_object_strategy.write.assert_called_once_with([mock_string])

    @mock.patch('xcrawler.files.writers.item_writer.object_utils.get_list_of_variable_values_sorted_by_name')
    def test_write_item_variables_to_output_file(self, mock_get_list_of_variable_values_sorted_by_name):
        mock_item = mock.Mock()
        mock_variables = { "width": 800, "height": 600, "title": "mock title"}
        mock_get_list_of_variable_values_sorted_by_name.return_value = [600, "mock title", 800]
        self.item_writer.write_item_to_output_file(mock_item)
        self.item_writer.write_object_strategy.write.assert_called_once_with(mock_get_list_of_variable_values_sorted_by_name.return_value)

    @mock.patch('xcrawler.files.writers.item_writer.create_csv_strategy')
    def test_open_output_file(self, mock_create_csv_strategy):
        mock_file_name = "mock_output.csv"
        mock_file = mock.Mock()
        mock_write_object_stategy = mock.Mock()
        self.item_writer.file_opener.open_file_write_strings.return_value = mock_file
        mock_create_csv_strategy.return_value = mock_write_object_stategy
        self.item_writer.open_output_file(mock_file_name)
    
        self.assertEquals(self.item_writer.output_file_name, mock_file_name)
        self.assertEquals(self.item_writer.output_file, mock_file)
        self.assertEquals(self.item_writer.write_object_strategy, mock_write_object_stategy)
           
    def test_close_output_file(self):
        self.item_writer.output_file = mock.Mock()
        self.item_writer.close_output_file()
        
        self.item_writer.output_file.close.assert_called_once_with()
        


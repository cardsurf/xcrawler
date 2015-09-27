
import unittest
import mock
import csv

import xcrawler

class TestItemWriter(unittest.TestCase):

    def setUp(self):
        self.item_writer = xcrawler.ItemWriter()
        self.item_writer.writer = mock.create_autospec(csv.writer).return_value
        self.item_writer._ItemWriter__no_items_written_to_file = True

    @mock.patch('xcrawler.files.item_writer.string_utils.is_string')
    def test_write_headers_to_output_file_string_argument(self, mock_is_string_function):
        mock_string = "mock"        
        mock_is_string_function.return_value = True

        self.item_writer.write_headers_to_output_file(mock_string)
        mock_is_string_function.assert_called_once_with(mock_string)
           
    @mock.patch('xcrawler.files.item_writer.string_utils.is_string')
    @mock.patch('__builtin__.vars')
    @mock.patch('__builtin__.sorted')
    def test_write_headers_to_output_file_item_argument(self, mock_sorted_function, mock_vars_function, mock_is_string_function):
        mock_item = mock.Mock()
        mock_variables = mock.Mock()
        mock_headers = mock.Mock()
        mock_is_string_function.return_value = False
        mock_vars_function.return_value = mock_variables
        mock_variables.keys.return_value = mock_headers
        mock_sorted_function.return_value = mock_headers
        self.item_writer.write_headers_to_output_file(mock_item)
        self.item_writer.writer.writerow.assert_called_once_with(mock_headers)
        
    @mock.patch.object(xcrawler.ItemWriter, 'write_headers_to_output_file') 
    @mock.patch.object(xcrawler.ItemWriter, 'write_item_to_output_file') 
    def test_write_item_first_item(self, mock_write_item_to_output_file, mock_write_headers_to_output_file):
        self.item_writer._ItemWriter__no_items_written_to_file = True
        mock_item = mock.Mock()
        self.item_writer.write_item(mock_item)
        self.assertFalse(self.item_writer._ItemWriter__no_items_written_to_file)
        
        mock_write_headers_to_output_file.assert_called_once_with(mock_item)
        mock_write_item_to_output_file.assert_called_once_with(mock_item)
        
    @mock.patch.object(xcrawler.ItemWriter, 'write_item_to_output_file') 
    def test_write_item_non_first_item(self, mock_write_item_to_output_file):
        self.item_writer._ItemWriter__no_items_written_to_file = False
        mock_item = mock.Mock()
        self.item_writer.write_item(mock_item)
        
        mock_write_item_to_output_file.assert_called_once_with(mock_item)
        
    @mock.patch('xcrawler.files.item_writer.string_utils.is_string')
    @mock.patch.object(xcrawler.ItemWriter, 'write_string_to_output_file') 
    def test_write_item_to_output_file_string_argument(self, mock_write_string_to_output_file, mock_is_string_function):
        mock_is_string_function.return_value = True
        mock_string = "mock"
        self.item_writer.write_item_to_output_file(mock_string)
        
        mock_is_string_function.assert_called_once_with(mock_string)
        mock_write_string_to_output_file.assert_called_once_with(mock_string)
        
    @mock.patch('xcrawler.files.item_writer.string_utils.is_string')
    @mock.patch.object(xcrawler.ItemWriter, 'write_item_variables_to_output_file') 
    def test_write_item_to_output_file_item_argument(self, mock_write_item_variables_to_output_file,
                                                      mock_is_string_function):
        mock_is_string_function.return_value = False
        mock_item = mock.Mock()
        self.item_writer.write_item_to_output_file(mock_item)
        
        mock_is_string_function.assert_called_once_with(mock_item)
        mock_write_item_variables_to_output_file.assert_called_once_with(mock_item)   
        
    @mock.patch('xcrawler.files.item_writer.string_utils.convert_string_to_utf8')
    def test_write_string_to_output_file(self, mock_convert_string_to_utf8):
        mock_convert_string_to_utf8.return_value = "mock_byte_string_utf8"
        mock_string = "mock"
        self.item_writer.write_string_to_output_file(mock_string)
        
        mock_convert_string_to_utf8.assert_called_once_with(mock_string)
        self.item_writer.writer.writerow.assert_called_once_with([mock_convert_string_to_utf8.return_value])
        
    @mock.patch('__builtin__.vars')
    @mock.patch('xcrawler.files.item_writer.dict_utils.get_list_of_values_sorted_by_keys')
    @mock.patch('xcrawler.files.item_writer.string_utils.list_convert_string_to_utf8')
    def test_write_item_variables_to_output_file(self, mock_list_convert_string_to_utf8_function,
                                                       mock_get_list_of_values_sorted_by_keys, mock_vars_function):
        mock_item = mock.Mock()
        mock_variables = mock.Mock()
        mock_values = mock.Mock()        
        mock_vars_function.return_value = mock_variables
        mock_get_list_of_values_sorted_by_keys.return_value = mock_values
        mock_list_convert_string_to_utf8_function.return_value = mock_get_list_of_values_sorted_by_keys.return_value
        self.item_writer.write_item_to_output_file(mock_item)
        self.item_writer.writer.writerow.assert_called_once_with(mock_values)

    @mock.patch('xcrawler.files.item_writer.csv.writer')
    @mock.patch('__builtin__.open')
    def test_open_output_file(self, mock_open_function, mock_csv_writer_function):
        mock_file_name = "mock_file_name"
        mock_file = mock.Mock()
        mock_writer = mock.Mock()
        mock_open_function.return_value = mock_file
        mock_csv_writer_function.return_value = mock_writer
        self.item_writer.open_output_file(mock_file_name)
    
        self.assertEquals(self.item_writer.output_file_name, mock_file_name)
        self.assertEquals(self.item_writer.output_file, mock_file)
        self.assertEquals(self.item_writer.writer, mock_writer)
           
    def test_close_output_file(self):
        self.item_writer.output_file = mock.Mock()
        self.item_writer.close_output_file()
        
        self.item_writer.output_file.close.assert_called_once_with()
        


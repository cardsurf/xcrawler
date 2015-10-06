
import unittest
import mock
import csv

from xcrawler.files.openers.file_opener_write import FileOpenerWrite
from xcrawler.files.strategies.writeobject.write_object_csv import WriteObjectCsv


class TestWriteObjectCsv(unittest.TestCase):

    def setUp(self):
        mock_file_opener = mock.create_autospec(FileOpenerWrite).return_value
        self.write_object_csv = WriteObjectCsv(mock_file_opener)
        self.write_object_csv.writer = mock.create_autospec(csv.writer).return_value
        self.write_object_csv.convert_to_strings_function = mock.Mock()

    @mock.patch('xcrawler.files.strategies.writeobject.write_object_csv.version_utils.is_python2')
    @mock.patch('xcrawler.files.strategies.writeobject.write_object_csv.string_utils.list_convert_to_byte_string_utf8')
    def test_get_convert_to_strings_python2(self, mock_list_convert_to_byte_string_utf8, mock_is_python2):
        mock_is_python2.return_value = True
        result = self.write_object_csv.get_convert_to_strings_function()
        self.assertEquals(result, mock_list_convert_to_byte_string_utf8)

    @mock.patch('xcrawler.files.strategies.writeobject.write_object_csv.version_utils.is_python2')
    @mock.patch('xcrawler.files.strategies.writeobject.write_object_csv.string_utils.list_convert_to_unicode_string')
    def test_get_convert_to_strings_python3(self, mock_list_convert_to_unicode_string, mock_is_python2):
        mock_is_python2.return_value = False
        result = self.write_object_csv.get_convert_to_strings_function()
        self.assertEquals(result, mock_list_convert_to_unicode_string)

    @mock.patch.object(WriteObjectCsv, 'open_file_and_init_writer')
    def test_open_file(self, mock_open_file_and_init_writer):
        mock_file_name = "mock.csv"
        mock_file = mock.Mock()
        mock_open_file_and_init_writer.return_value = mock_file
        result = self.write_object_csv.open_file(mock_file_name)
        self.assertEquals(result, mock_file)

    @mock.patch.object(WriteObjectCsv, 'init_writer')
    def test_open_and_init_writer(self, mock_init_writer):
        mock_file_name = "mock.csv"
        mock_file = mock.Mock()
        self.write_object_csv.file_opener.open_file_write_strings.return_value = mock_file
        result = self.write_object_csv.open_file(mock_file_name)
        mock_init_writer.assert_called_once_with(mock_file)
        self.assertEquals(result, mock_file)

    @mock.patch('xcrawler.files.strategies.writeobject.write_object_csv.csv.writer')
    def test_init_writer(self, mock_csv_writer_class):
        mock_file = mock.Mock()
        self.write_object_csv.init_writer(mock_file)
        self.assertEquals(mock_csv_writer_class.call_count, 1)

    @mock.patch('xcrawler.files.strategies.writeobject.write_object_csv.string_utils.is_string')
    def test_write_headers_string_argument(self, mock_is_string_function):
        mock_string = "mock"
        mock_is_string_function.return_value = True

        self.write_object_csv.write_headers(mock_string)
        mock_is_string_function.assert_called_once_with(mock_string)

    @mock.patch('xcrawler.files.strategies.writeobject.write_object_csv.string_utils.is_string')
    @mock.patch('xcrawler.files.strategies.writeobject.write_object_csv.object_utils.get_list_of_variable_names_sorted_by_name')
    @mock.patch.object(WriteObjectCsv, 'write')
    def test_write_headers_item_argument(self, mock_write, mock_get_list_of_variable_names_sorted_by_name, mock_is_string_function):
        mock_item = mock.Mock()
        mock_item_variables = { "width": 800, "height": 600, "title": "mock title" }
        mock_names = ["height", "mock title", "width"]
        mock_is_string_function.return_value = False
        mock_get_list_of_variable_names_sorted_by_name.return_value = ["height", "mock title", "width"]
        self.write_object_csv.write_headers(mock_item)
        mock_write.assert_called_once_with(mock_names)

    @mock.patch('xcrawler.files.strategies.writeobject.write_object_csv.string_utils.is_string')
    @mock.patch.object(WriteObjectCsv, 'write')
    def test_write_item_string_argument(self, mock_write, mock_is_string):
        mock_item = "Mock string"
        mock_is_string.return_value = True
        self.write_object_csv.write_item(mock_item)
        mock_write.assert_called_once_with([mock_item])

    @mock.patch('xcrawler.files.strategies.writeobject.write_object_csv.string_utils.is_string')
    @mock.patch.object(WriteObjectCsv, 'write_variables')
    def test_write_item_non_string_argument(self, mock_write_variables, mock_is_string):
        mock_item = mock.Mock()
        mock_is_string.return_value = False
        self.write_object_csv.write_item(mock_item)
        mock_write_variables.assert_called_once_with(mock_item)

    @mock.patch('xcrawler.files.strategies.writeobject.write_object_csv.object_utils.get_list_of_variable_values_sorted_by_name')
    @mock.patch.object(WriteObjectCsv, 'write')
    def test_write_variable_values(self, mock_write, mock_get_list_of_variable_values_sorted_by_name):
        mock_object = mock.Mock()
        mock_object_variables = { "width": 800, "height": 600, "title": "mock title" }
        mock_get_list_of_variable_values_sorted_by_name.return_value = [600, "mock title", 800]
        self.write_object_csv.convert_to_strings_function.return_value = ["600", "mock title", "800"]
        self.write_object_csv.write_variables(mock_object)
        mock_write.assert_called_once_with(self.write_object_csv.convert_to_strings_function.return_value)

    def test_write(self):
        mock_list_string = ["600", "mock title", "800"]
        self.write_object_csv.write(mock_list_string)
        self.write_object_csv.writer.writerow.assert_called_once_with(mock_list_string)
import unittest
import csv

import mock

from xcrawler.files.writers.object_writer_csv import ObjectWriterCsv
from xcrawler.compatibility.compatible_file_opener_write import CompatibleFileOpenerWrite
from xcrawler.compatibility.compatible_object_string_converter import CompatibleObjectStringConverter


class TestWriteObjectCsv(unittest.TestCase):

    def setUp(self):
        mock_file_opener = mock.create_autospec(CompatibleFileOpenerWrite).return_value
        mock_object_to_string_converter = mock.create_autospec(CompatibleObjectStringConverter).return_value
        self.object_writer_csv = ObjectWriterCsv(mock_file_opener, mock_object_to_string_converter)
        self.object_writer_csv.writer = mock.create_autospec(csv.writer).return_value
        self.object_writer_csv.convert_to_strings_function = mock.Mock()

    @mock.patch.object(ObjectWriterCsv, 'open_file_and_init_writer')
    def test_open_file(self, mock_open_file_and_init_writer):
        mock_file_name = "mock.csv"
        mock_file = mock.Mock()
        mock_open_file_and_init_writer.return_value = mock_file
        result = self.object_writer_csv.open_file(mock_file_name)
        self.assertEquals(result, mock_file)

    @mock.patch.object(ObjectWriterCsv, 'init_writer')
    def test_open_and_init_writer(self, mock_init_writer):
        mock_file_name = "mock.csv"
        mock_file = mock.Mock()
        self.object_writer_csv.file_opener.open_file_write_strings.return_value = mock_file
        result = self.object_writer_csv.open_file(mock_file_name)
        mock_init_writer.assert_called_once_with(mock_file)
        self.assertEquals(result, mock_file)

    @mock.patch('xcrawler.files.writers.object_writer_csv.csv.writer')
    def test_init_writer(self, mock_csv_writer_class):
        mock_file = mock.Mock()
        self.object_writer_csv.init_writer(mock_file)
        self.assertEquals(mock_csv_writer_class.call_count, 1)

    @mock.patch('xcrawler.files.writers.object_writer_csv.string_utils.is_string')
    def test_write_headers_string_argument(self, mock_is_string_function):
        mock_string = "mock"
        mock_is_string_function.return_value = True

        self.object_writer_csv.write_headers(mock_string)
        mock_is_string_function.assert_called_once_with(mock_string)

    @mock.patch('xcrawler.files.writers.object_writer_csv.string_utils.is_string')
    @mock.patch('xcrawler.files.writers.object_writer_csv.object_utils.get_list_of_variable_names_sorted_by_name')
    @mock.patch.object(ObjectWriterCsv, 'write')
    def test_write_headers_item_argument(self, mock_write, mock_get_list_of_variable_names_sorted_by_name, mock_is_string_function):
        mock_item = mock.Mock()
        mock_item_variables = { "width": 800, "height": 600, "title": "mock title" }
        mock_names = ["height", "mock title", "width"]
        mock_is_string_function.return_value = False
        mock_get_list_of_variable_names_sorted_by_name.return_value = ["height", "mock title", "width"]
        self.object_writer_csv.write_headers(mock_item)
        mock_write.assert_called_once_with(mock_names)

    @mock.patch('xcrawler.files.writers.object_writer_csv.string_utils.is_string')
    @mock.patch.object(ObjectWriterCsv, 'write')
    def test_write_item_string_argument(self, mock_write, mock_is_string):
        mock_item = "Mock string"
        mock_is_string.return_value = True
        self.object_writer_csv.write_item(mock_item)
        mock_write.assert_called_once_with([mock_item])

    @mock.patch('xcrawler.files.writers.object_writer_csv.string_utils.is_string')
    @mock.patch.object(ObjectWriterCsv, 'write_variables')
    def test_write_item_non_string_argument(self, mock_write_variables, mock_is_string):
        mock_item = mock.Mock()
        mock_is_string.return_value = False
        self.object_writer_csv.write_item(mock_item)
        mock_write_variables.assert_called_once_with(mock_item)

    @mock.patch('xcrawler.files.writers.object_writer_csv.object_utils.get_list_of_variable_values_sorted_by_name')
    @mock.patch.object(ObjectWriterCsv, 'write')
    def test_write_variable_values(self, mock_write, mock_get_list_of_variable_values_sorted_by_name):
        mock_object = mock.Mock()
        mock_object_variables = { "width": 800, "height": 600, "title": "mock title" }
        mock_get_list_of_variable_values_sorted_by_name.return_value = [600, "mock title", 800]
        self.object_writer_csv.object_to_string_converter.list_convert_to_string.return_value = ["600", "mock title", "800"]
        self.object_writer_csv.write_variables(mock_object)
        mock_write.assert_called_once_with(self.object_writer_csv.object_to_string_converter.list_convert_to_string.return_value)

    def test_write(self):
        mock_list_string = ["600", "mock title", "800"]
        self.object_writer_csv.write(mock_list_string)
        self.object_writer_csv.writer.writerow.assert_called_once_with(mock_list_string)

import unittest
import mock
import csv

from xcrawler.files.writers.object_writer_csv import ObjectWriterCsv
from xcrawler.compatibility.write_opener.compatible_write_opener import CompatibleWriteOpener
from xcrawler.compatibility.object_converter.compatible_object_converter import CompatibleObjectConverter
from xcrawler.pythonutils.sorters.variables_sorter import VariablesSorter
from xcrawler.pythonutils.types.instance_resolver import InstanceResolver
from xcrawler.files.writers.csv_writer import CsvWriterFactory


class TestObjectWriterCsv(unittest.TestCase):

    def setUp(self):
        file_opener = mock.create_autospec(CompatibleWriteOpener).return_value
        object_converter = mock.create_autospec(CompatibleObjectConverter).return_value
        variables_sorter = mock.create_autospec(VariablesSorter).return_value
        instance_resolver = mock.create_autospec(InstanceResolver).return_value
        csv_writer_factory = mock.create_autospec(CsvWriterFactory).return_value
        self.object_writer_csv = ObjectWriterCsv(file_opener, object_converter, variables_sorter, 
                                                 instance_resolver, csv_writer_factory)
        self.object_writer_csv.writer = mock.create_autospec(csv.writer).return_value
        self.object_writer_csv.convert_to_strings_function = mock.Mock()

    @mock.patch.object(ObjectWriterCsv, 'open_file_and_create_writer')
    def test_open_file(self, mock_open_file_and_create_writer):
        mock_file_name = "mock.csv"
        mock_file = mock.Mock()
        mock_open_file_and_create_writer.return_value = mock_file
        result = self.object_writer_csv.open_file(mock_file_name)
        self.assertEquals(result, mock_file)

    def test_open_and_create_writer(self):
        mock_file_name = "mock.csv"
        mock_file = mock.Mock()
        mock_csv_writer = mock.create_autospec(csv.writer).return_value
        self.object_writer_csv.file_opener.open_file_write_strings.return_value = mock_file
        self.object_writer_csv.csv_writer_factory.create_csv_writer.return_value = mock_csv_writer
        result = self.object_writer_csv.open_file_and_create_writer(mock_file_name)
        self.assertEquals(self.object_writer_csv.writer, mock_csv_writer)
        self.assertEquals(result, mock_file)

    def test_write_headers_string_argument(self):
        mock_string = "mock"
        self.object_writer_csv.instance_resolver.is_unicode_or_byte_string.return_value = True
        self.object_writer_csv.write_headers(mock_string)
        self.object_writer_csv.instance_resolver.is_unicode_or_byte_string.assert_called_once_with(mock_string)

    @mock.patch.object(ObjectWriterCsv, 'write')
    def test_write_headers_object_argument(self, mock_write):
        mock_object = mock.Mock()
        mock_object_variables = { "width": 800, "height": 600, "title": "mock title" }
        mock_names = ["height", "mock title", "width"]
        self.object_writer_csv.instance_resolver.is_unicode_or_byte_string.return_value = False
        self.object_writer_csv.variables_sorter.get_list_of_variable_names_sorted_by_name.return_value = ["height", "mock title", "width"]
        self.object_writer_csv.write_headers(mock_object)
        mock_write.assert_called_once_with(mock_names)

    @mock.patch.object(ObjectWriterCsv, 'write')
    def test_write_object_string_argument(self, mock_write):
        mock_object = "Mock string"
        self.object_writer_csv.instance_resolver.is_unicode_or_byte_string.return_value = True
        self.object_writer_csv.write_object(mock_object)
        mock_write.assert_called_once_with([mock_object])

    @mock.patch.object(ObjectWriterCsv, 'write_variables')
    def test_write_object_non_string_argument(self, mock_write_variables):
        mock_object = mock.Mock()
        self.object_writer_csv.instance_resolver.is_unicode_or_byte_string.return_value = False
        self.object_writer_csv.write_object(mock_object)
        mock_write_variables.assert_called_once_with(mock_object)

    @mock.patch.object(ObjectWriterCsv, 'write')
    def test_write_variable_values(self, mock_write):
        mock_object = mock.Mock()
        mock_object_variables = { "width": 800, "height": 600, "title": b"mock\x00title" }
        self.object_writer_csv.variables_sorter.get_list_of_variable_values_sorted_by_name.return_value = [600, b"mock\x00title", 800]
        self.object_writer_csv.object_converter.list_convert_to_string.return_value = ["600", b"mock\x00title", "800"]
        self.object_writer_csv.write_variables(mock_object)
        mock_write.assert_called_once_with(self.object_writer_csv.object_converter.list_convert_to_string.return_value)

    def test_write(self):
        mock_list_string = ["600", "mock title", "800"]
        self.object_writer_csv.write(mock_list_string)
        self.object_writer_csv.writer.writerow.assert_called_once_with(mock_list_string)
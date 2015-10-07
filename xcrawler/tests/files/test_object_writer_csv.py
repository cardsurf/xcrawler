
import unittest
import mock
import csv

from xcrawler.files.writers.object_writer_csv import ObjectWriterCsv
from xcrawler.compatibility.write_opener.compatible_write_opener import CompatibleWriteOpener
from xcrawler.compatibility.object_converter.compatible_object_converter import CompatibleObjectConverter
from xcrawler.utils.sorters.variables_sorter import VariablesSorter
from xcrawler.utils.types.instance_resolver import InstanceResolver


class TestObjectWriterCsv(unittest.TestCase):

    def setUp(self):
        file_opener = mock.create_autospec(CompatibleWriteOpener).return_value
        object_converter = mock.create_autospec(CompatibleObjectConverter).return_value
        variables_sorter = mock.create_autospec(VariablesSorter).return_value
        instance_resolver = mock.create_autospec(InstanceResolver).return_value
        self.object_writer_csv = ObjectWriterCsv(file_opener, object_converter, variables_sorter, instance_resolver)
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

    def test_write_headers_string_argument(self):
        mock_string = "mock"
        self.object_writer_csv.instance_resolver.is_string.return_value = True
        self.object_writer_csv.write_headers(mock_string)
        self.object_writer_csv.instance_resolver.is_string.assert_called_once_with(mock_string)

    @mock.patch.object(ObjectWriterCsv, 'write')
    def test_write_headers_object_argument(self, mock_write):
        mock_object = mock.Mock()
        mock_object_variables = { "width": 800, "height": 600, "title": "mock title" }
        mock_names = ["height", "mock title", "width"]
        self.object_writer_csv.instance_resolver.is_string.return_value = False
        self.object_writer_csv.variables_sorter.get_list_of_variable_names_sorted_by_name.return_value = ["height", "mock title", "width"]
        self.object_writer_csv.write_headers(mock_object)
        mock_write.assert_called_once_with(mock_names)

    @mock.patch.object(ObjectWriterCsv, 'write')
    def test_write_object_string_argument(self, mock_write):
        mock_object = "Mock string"
        self.object_writer_csv.instance_resolver.is_string.return_value = True
        self.object_writer_csv.write_object(mock_object)
        mock_write.assert_called_once_with([mock_object])

    @mock.patch.object(ObjectWriterCsv, 'write_variables')
    def test_write_object_non_string_argument(self, mock_write_variables):
        mock_object = mock.Mock()
        self.object_writer_csv.instance_resolver.is_string.return_value = False
        self.object_writer_csv.write_object(mock_object)
        mock_write_variables.assert_called_once_with(mock_object)

    @mock.patch.object(ObjectWriterCsv, 'write')
    def test_write_variable_values(self, mock_write):
        mock_object = mock.Mock()
        mock_object_variables = { "width": 800, "height": 600, "title": "mock title" }
        self.object_writer_csv.variables_sorter.get_list_of_variable_values_sorted_by_name.return_value = [600, "mock title", 800]
        self.object_writer_csv.object_converter.list_convert_to_string.return_value = ["600", "mock title", "800"]
        self.object_writer_csv.write_variables(mock_object)
        mock_write.assert_called_once_with(self.object_writer_csv.object_converter.list_convert_to_string.return_value)

    def test_write(self):
        mock_list_string = ["600", "mock title", "800"]
        self.object_writer_csv.write(mock_list_string)
        self.object_writer_csv.writer.writerow.assert_called_once_with(mock_list_string)
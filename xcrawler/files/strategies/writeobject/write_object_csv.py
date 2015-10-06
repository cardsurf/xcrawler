
import csv

from xcrawler.pythonutils import string_utils
from xcrawler.pythonutils import object_utils
from xcrawler.pythonutils import version_utils
from xcrawler.files.strategies.writeobject.write_object_strategy import WriteObjectStrategy


class WriteObjectCsv(WriteObjectStrategy):
    """A base strategy of writing objects to a .csv file."

    """

    def __init__(self, file_opener):
        self.file_opener = file_opener
        self.convert_to_strings_function = self.get_convert_to_strings_function()
        self.writer = None

    def get_convert_to_strings_function(self):
        if version_utils.is_python2():
            return string_utils.list_convert_to_byte_string_utf8
        else:
            return string_utils.list_convert_to_unicode_string

    def open_file(self, file_name):
        output_file = self.open_file_and_init_writer(file_name)
        return output_file

    def open_file_and_init_writer(self, file_name):
        output_file = self.file_opener.open_file_write_strings(file_name)
        self.init_writer(output_file)
        return output_file

    def init_writer(self, opened_file):
        self.writer = csv.writer(opened_file, delimiter=' ', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')

    def write_headers(self, item):
        if not string_utils.is_string(item):
            headers = object_utils.get_list_of_variable_names_sorted_by_name(item)
            self.write(headers)

    def write_item(self, item):
        if string_utils.is_string(item):
            self.write([item])
        else:
            self.write_variables(item)

    def write_variables(self, item):
        values = object_utils.get_list_of_variable_values_sorted_by_name(item)
        values = self.convert_to_strings_function(values)
        self.write(values)

    def write(self, list_strings):
        self.writer.writerow(list_strings)

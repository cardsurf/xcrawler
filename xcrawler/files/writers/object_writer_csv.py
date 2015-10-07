import csv

from xcrawler.utils import string_utils
from xcrawler.utils import object_utils
from xcrawler.files.writers.object_writer import ObjectWriter


class ObjectWriterCsv(ObjectWriter):
    """Writes objects to a .csv file."

    """

    def __init__(self, file_opener, object_to_string_converter):
        self.file_opener = file_opener
        self.object_to_string_converter = object_to_string_converter
        self.writer = None

    def open_file(self, file_name):
        output_file = self.open_file_and_init_writer(file_name)
        return output_file

    def open_file_and_init_writer(self, file_name):
        output_file = self.file_opener.open_file_write_strings(file_name)
        self.init_writer(output_file)
        return output_file

    def init_writer(self, opened_file):
        self.writer = csv.writer(opened_file, delimiter=' ', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')

    def write_headers(self, instance_object):
        if not string_utils.is_string(instance_object):
            headers = object_utils.get_list_of_variable_names_sorted_by_name(instance_object)
            self.write(headers)

    def write_object(self, instance_object):
        if string_utils.is_string(instance_object):
            self.write([instance_object])
        else:
            self.write_variables(instance_object)

    def write_variables(self, instance_object):
        values = object_utils.get_list_of_variable_values_sorted_by_name(instance_object)
        values = self.object_to_string_converter.list_convert_to_string(values)
        self.write(values)

    def write(self, list_strings):
        self.writer.writerow(list_strings)

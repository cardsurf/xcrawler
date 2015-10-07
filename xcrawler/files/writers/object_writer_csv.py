import csv

from xcrawler.utils import string_utils
from xcrawler.utils.sorters.variables_sorter import VariablesSorter
from xcrawler.files.writers.object_writer import ObjectWriter
from xcrawler.compatibility.write_opener.compatible_write_opener import CompatibleWriteOpener
from xcrawler.compatibility.object_converter.compatible_object_converter import CompatibleObjectConverter


class ObjectWriterCsv(ObjectWriter):
    """Writes objects to a .csv file."

    """

    def __init__(self, file_opener=CompatibleWriteOpener(),
                 object_converter=CompatibleObjectConverter(),
                 variables_sorter=VariablesSorter()):
        self.file_opener = file_opener
        self.object_converter = object_converter
        self.variables_sorter = variables_sorter
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
            headers = self.variables_sorter.get_list_of_variable_names_sorted_by_name(instance_object)
            self.write(headers)

    def write_object(self, instance_object):
        if string_utils.is_string(instance_object):
            self.write([instance_object])
        else:
            self.write_variables(instance_object)

    def write_variables(self, instance_object):
        values = self.variables_sorter.get_list_of_variable_values_sorted_by_name(instance_object)
        values = self.object_converter.list_convert_to_string(values)
        self.write(values)

    def write(self, list_strings):
        self.writer.writerow(list_strings)

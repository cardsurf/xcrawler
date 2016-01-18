
import csv

from xcrawler.pythonutils.types.instance_resolver import InstanceResolver
from xcrawler.pythonutils.sorters.variables_sorter import VariablesSorter
from xcrawler.files.writers.object_writer import ObjectWriter
from xcrawler.compatibility.write_opener.compatible_write_opener import CompatibleWriteOpener
from xcrawler.compatibility.object_converter.compatible_object_converter import CompatibleObjectConverter
from xcrawler.files.writers.csv_writer import CsvWriterFactory


class ObjectWriterCsv(ObjectWriter):
    """Writes objects to a .csv file."

    """
    def __init__(self,
                 file_opener=CompatibleWriteOpener(),
                 object_converter=CompatibleObjectConverter(),
                 variables_sorter=VariablesSorter(),
                 instance_resolver=InstanceResolver(),
                 csv_writer_factory=CsvWriterFactory()):
        self.file_opener = file_opener
        self.object_converter = object_converter
        self.variables_sorter = variables_sorter
        self.instance_resolver = instance_resolver
        self.csv_writer_factory = csv_writer_factory
        self.writer = None

    def open_file(self, file_name):
        output_file = self.open_file_and_create_writer(file_name)
        return output_file

    def open_file_and_create_writer(self, file_name):
        output_file = self.file_opener.open_file_write_strings(file_name)
        self.writer = self.csv_writer_factory.create_csv_writer(output_file)
        return output_file

    def write_headers(self, instance_object):
        if not self.instance_resolver.is_unicode_or_byte_string(instance_object):
            headers = self.variables_sorter.get_list_of_variable_names_sorted_by_name(instance_object)
            self.write(headers)

    def write_object(self, instance_object):
        if self.instance_resolver.is_unicode_or_byte_string(instance_object):
            self.write([instance_object])
        else:
            self.write_variables(instance_object)

    def write_variables(self, instance_object):
        values = self.variables_sorter.get_list_of_variable_values_sorted_by_name(instance_object)
        values = self.object_converter.list_convert_to_string(values)
        self.write(values)

    def write(self, list_strings):
        self.writer.writerow(list_strings)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xcrawler.pythonutils import string_utils
from xcrawler.pythonutils import object_utils
from xcrawler.files.openers.file_opener_write import FileOpenerWrite
from xcrawler.files.strategies.writeobject.factory import create_csv_strategy


class ItemWriter:
    """Writes data extracted from web pages to an output file.
    
    """
    def __init__(self):
        self.__no_items_written_to_file = True
        self.output_file_name = ""
        self.output_file = None
        self.file_opener = FileOpenerWrite()
        self.write_object_strategy = None

    def write_headers_to_output_file(self, item):             
        if not string_utils.is_string(item):
            headers = object_utils.get_list_of_variable_names_sorted_by_name(item)
            self.write_object_strategy.write(headers)

    def write_item(self, item):
        if self.__no_items_written_to_file:
            self.write_headers_to_output_file(item)
            self.__no_items_written_to_file = False   
               
        self.write_item_to_output_file(item)

    def write_item_to_output_file(self, item):
        if string_utils.is_string(item):
            self.write_string_to_output_file(item)
        else:
            self.write_item_variables_to_output_file(item)

    def write_string_to_output_file(self, string):
        self.write_object_strategy.write([string])

    def write_item_variables_to_output_file(self, item):
        values = object_utils.get_list_of_variable_values_sorted_by_name(item)
        self.write_object_strategy.write(values)

    def open_output_file(self, output_file_name):
        self.output_file_name = output_file_name
        self.output_file = self.file_opener.open_file_write_strings(output_file_name)
        self.write_object_strategy = create_csv_strategy(self.output_file)

    def close_output_file(self):
        self.output_file.close()


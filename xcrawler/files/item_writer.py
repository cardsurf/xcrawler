#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from ..pythonutils import string_utils
from ..pythonutils import dict_utils

class ItemWriter(object):
    """Writes data extracted from web pages to an output file.
    
    """
    def __init__(self):
        self.__no_items_written_to_file = True
        
    def write_headers_to_output_file(self, item):             
        if not string_utils.is_string(item):
            variables = vars(item)
            headers = variables.keys()
            headers = sorted(headers)
            self.writer.writerow(headers)
     
    def write_item(self, item):
        if(self.__no_items_written_to_file):
            self.write_headers_to_output_file(item)
            self.__no_items_written_to_file = False   
               
        self.write_item_to_output_file(item)

    def write_item_to_output_file(self, item):
        if string_utils.is_string(item):
            self.write_string_to_output_file(item)
        else:
            self.write_item_variables_to_output_file(item)

    def write_string_to_output_file(self, string):
        string = string_utils.convert_string_to_unicode(string)
        self.writer.writerow([string])
    
    def write_item_variables_to_output_file(self, item):
        variables = vars(item)
        values = dict_utils.get_list_of_values_sorted_by_keys(variables)
        values = string_utils.list_convert_string_to_unicode(values)
        self.writer.writerow(values)

    def open_output_file(self, output_file_name):
        self.output_file_name = output_file_name
        self.output_file = open(self.output_file_name, "wb", )
        self.writer = csv.writer(self.output_file, delimiter=' ', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n') 

    def close_output_file(self):
        self.output_file.close()
        

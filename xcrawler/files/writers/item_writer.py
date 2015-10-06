#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xcrawler.compatibility.compatibility_factory import CompatibilityFactory
from xcrawler.files.writers.object_writer_csv import ObjectWriterCsv


class ItemWriter:
    """Writes data extracted from web pages to an output file.
    
    """
    def __init__(self):
        self.__no_items_written_to_file = True
        self.output_file_name = ""
        self.output_file = None
        self.file_opener = CompatibilityFactory().create_compatible_file_opener_write()
        self.object_to_string_converter = CompatibilityFactory().create_compatible_object_string_converter()
        self.write_object_strategy = ObjectWriterCsv(self.file_opener, self.object_to_string_converter)

    def write_headers(self, item):
        self.write_object_strategy.write_headers(item)

    def write_item(self, item):
        if self.__no_items_written_to_file:
            self.write_headers(item)
            self.__no_items_written_to_file = False   

        self.write_object_strategy.write_object(item)

    def open_output_file(self, output_file_name):
        self.output_file = self.write_object_strategy.open_file(output_file_name)

    def close_output_file(self):
        self.output_file.close()


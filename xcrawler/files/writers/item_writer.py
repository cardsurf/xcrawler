#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xcrawler.files.openers.file_opener_write import FileOpenerWrite
from xcrawler.files.strategies.writeobject.write_object_csv import WriteObjectCsv


class ItemWriter:
    """Writes data extracted from web pages to an output file.
    
    """
    def __init__(self):
        self.__no_items_written_to_file = True
        self.output_file_name = ""
        self.output_file = None
        self.file_opener = FileOpenerWrite()
        self.write_object_strategy = None

    def write_headers(self, item):
        self.write_object_strategy.write_headers(item)

    def write_item(self, item):
        if self.__no_items_written_to_file:
            self.write_headers(item)
            self.__no_items_written_to_file = False   

        self.write_object_strategy.write_item(item)

    def open_output_file(self, output_file_name):
        self.output_file_name = output_file_name
        self.output_file = self.file_opener.open_file_write_strings(output_file_name)
        self.write_object_strategy = WriteObjectCsv(self.output_file)

    def close_output_file(self):
        self.output_file.close()


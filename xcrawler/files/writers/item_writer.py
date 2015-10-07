#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ItemWriter:
    """Writes data extracted from web pages to an output file.
    
    """
    def __init__(self, object_writer):
        self.__no_items_written_to_file = True
        self.output_file_name = ""
        self.output_file = None
        self.object_writer = object_writer

    def write_headers(self, item):
        self.object_writer.write_headers(item)

    def write_item(self, item):
        if self.__no_items_written_to_file:
            self.write_headers(item)
            self.__no_items_written_to_file = False   

        self.object_writer.write_object(item)

    def open_output_file(self, output_file_name):
        self.output_file = self.object_writer.open_file(output_file_name)

    def close_output_file(self):
        self.output_file.close()


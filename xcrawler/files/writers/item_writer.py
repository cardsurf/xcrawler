#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xcrawler.files.writers.object_writer_factory import ObjectWriterFactory
from xcrawler.files.filepaths.filepath_splitter import FilePathSplitter


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




class ItemWriterFactory:
    """Creates an instance of the ItemWriter class.

    """
    def __init__(self,
                 filepath_splitter=FilePathSplitter(),
                 object_writer_factory=ObjectWriterFactory()):
        self.filepath_splitter = filepath_splitter
        self.object_writer_factory = object_writer_factory

    def create_item_writer_based_on_file_extension(self, file_name):
        extension = self.filepath_splitter.get_file_extension(file_name)
        if extension == ".csv":
            return self.create_item_writer_csv()

        raise ValueError("Not supported file extension: " + extension)

    def create_item_writer_csv(self):
        object_writer_csv = self.object_writer_factory.create_object_writer_csv()
        item_writer = ItemWriter(object_writer_csv)
        return item_writer




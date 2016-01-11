
from __future__ import print_function
import threading

from xcrawler.core.crawler.config import Config
from xcrawler.files.writers.item_writer import ItemWriterFactory
from xcrawler.files.filepaths.filepath_splitter import FilePathSplitter
from xcrawler.files.writers.binary_writer import BinaryWriter
from xcrawler.files.writers.object_writer_csv import ObjectWriterCsv


class ItemProcessor(threading.Thread):
    """A thread that processes data extracted from web pages.
    
    """
    def __init__(self,
                 config,
                 items_queue,
                 filepath_splitter=FilePathSplitter(),
                 binary_writer=BinaryWriter()):
        threading.Thread.__init__(self)
        self.config = config
        self.items_queue = items_queue
        self.filepath_splitter = filepath_splitter
        self.binary_writer = binary_writer
        self.item_writer = None
        self.no_items_received = True

    def run(self):
        while True:
            item = self.items_queue.get()
            self.process_item(item)
            self.items_queue.task_done()  
        
    def process_item(self, item):
        if self.config.output_mode == Config.OUTPUT_MODE_PRINT:
            print(item)
        elif self.config.output_mode == Config.OUTPUT_MODE_FILE:
            self.item_writer.write_item(item)
    
    def open_output_file_if_needed(self):
        if self.config.output_mode == Config.OUTPUT_MODE_FILE:
            item_writer_factory = ItemWriterFactory()
            self.item_writer = item_writer_factory.create_item_writer_based_on_file_extension(self.config.output_file_name)
            self.item_writer.open_output_file(self.config.output_file_name)
        
    def close_output_file_if_needed(self):
        if self.config.output_mode == Config.OUTPUT_MODE_FILE:
            self.item_writer.close_output_file()
            self.fix_csv_writer_null_byte_bug()

    def close_output_file_if_needed(self):
        if self.config.output_mode == Config.OUTPUT_MODE_FILE:
            self.item_writer.close_output_file()
            self.fix_csv_writer_null_byte_bug()

    def fix_csv_writer_null_byte_bug(self):
        file_name = self.config.output_file_name
        extension = self.filepath_splitter.get_file_extension(file_name)
        if extension == ".csv":
            self.replace_placeholder_with_null_byte(file_name)

    def replace_placeholder_with_null_byte(self, file_name):
        self.binary_writer.replace(file_name,
                                   ObjectWriterCsv.CSV_WRITER_NULL_BYTE_PLACEHOLDER,
                                   ObjectWriterCsv.CSV_WRITER_NULL_BYTE)

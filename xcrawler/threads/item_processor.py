
from __future__ import print_function
import threading

from xcrawler.core.config import Config
from xcrawler.files.item_writer import ItemWriter

class ItemProcessor(threading.Thread):
    """Thread that process data extracted from web pages.
    
    """
    
    def __init__(self, config, items_queue):
        threading.Thread.__init__(self)
        self.config = config
        self.items_queue = items_queue
        self.item_writer = None
        self.no_items_received = True

    def run(self):
        while True:
            item = self.items_queue.get()
            self.process_item(item)
            self.items_queue.task_done()  
        
    def process_item(self, item):
        if(self.config.output_mode == Config.OUTPUT_MODE_PRINT):
            print(item)
        elif(self.config.output_mode == Config.OUTPUT_MODE_FILE):
            self.item_writer.write_item(item)
    
    def open_output_file_if_needed(self):
        if(self.config.output_mode == Config.OUTPUT_MODE_FILE):
            self.item_writer = ItemWriter()
            self.item_writer.open_output_file(self.config.output_file_name)
        
    def close_output_file_if_needed(self):
        if(self.config.output_mode == Config.OUTPUT_MODE_FILE):
            self.item_writer.close_output_file()
        
            
            
            
            
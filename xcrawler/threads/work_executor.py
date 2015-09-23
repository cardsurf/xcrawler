
import Queue

from page_processor import PageProcessor
from item_processor import ItemProcessor
from ..core.page import Page

class WorkExecutor():
    """Manages a process of visiting web pages.
    
    """
    
    def __init__(self, config):
        self.page_queue = Queue.Queue()
        self.item_queue = Queue.Queue()
        self.config = config
        self.spawn_worker_threads()

    def spawn_worker_threads(self):
        self.spawn_page_queue_threads()
        self.spawn_item_queue_thread()
    
    def spawn_page_queue_threads(self):
        for _ in range (self.config.number_of_threads):
            t = PageProcessor(self.config, self.page_queue, self.item_queue)
            t.daemon = True
            t.start()
            
    def spawn_item_queue_thread(self):
            self.item_processor = ItemProcessor(self.config, self.item_queue)
            self.item_processor.daemon = True
            self.item_processor.start()
        
    def execute_work(self, crawler):
        self.item_processor.open_output_file_if_needed()
        self.add_pages_to_queue(crawler)
        self.wait_until_work_is_done()
        self.item_processor.close_output_file_if_needed()
    
    def add_pages_to_queue(self, crawler):
        start_urls = crawler.start_urls
        page_scraper = crawler.get_first_page_scraper()
        
        for url in start_urls:
            page = Page(url, page_scraper)
            self.page_queue.put(page)

    def wait_until_work_is_done(self):
        self.page_queue.join()
        self.item_queue.join()
        

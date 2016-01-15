
import threading
import time

from xcrawler.http.requests.request_sender import RequestSender


class PageProcessor(threading.Thread):
    """A thread that fetches a web page.

    """
    def __init__(self,
                 config,
                 page_queue,
                 items_queue,
                 request_sender=RequestSender()):
        threading.Thread.__init__(self)
        self.config = config
        self.page_queue = page_queue
        self.items_queue = items_queue
        self.request_sender = request_sender
        self.request_sender.session = self.config.session
        self.request_sender.timeout = self.config.request_timeout

    def run(self):
        while True:
            page = self.page_queue.get()
            self.wait_to_fetch_page()
            self.process_page(page)
            self.page_queue.task_done()  
        
    def wait_to_fetch_page(self):
        time.sleep(self.config.fetch_delay)
        
    def process_page(self, page):
        page.request_sender.session = self.config.session
        page.request_sender.timeout = self.config.request_timeout
        page.content = self.request_sender.get_element(page.request)
        self.put_extracted_items_in_queue(page)
        self.put_extracted_pages_in_queue(page)

    def put_extracted_pages_in_queue(self, page):
        extracted_pages = page.extract_pages()
        for page in extracted_pages:
            self.page_queue.put(page) 

    def put_extracted_items_in_queue(self, page):
        extracted_items = page.extract_items()
        for item in extracted_items:
            self.items_queue.put(item)



from __future__ import print_function
import threading
import urllib2
import time
from httplib import BadStatusLine
import socket

class PageProcessor(threading.Thread):
    """Thread used to fetch a web page content.
    
    """
    
    def __init__(self, config, page_queue, items_queue):
        threading.Thread.__init__(self)
        self.config = config
        self.page_queue = page_queue
        self.items_queue = items_queue

    def run(self):
        while True:
            page = self.page_queue.get()
            self.wait_to_fetch_page()
            self.process_page(page)
            self.page_queue.task_done()  
        
    def wait_to_fetch_page(self):
        time.sleep(self.config.fetch_delay)
        
    def process_page(self, page):
        try:
            page.fetch_content()
            self.put_extracted_items_in_queue(page)
            self.put_extracted_pages_in_queue(page)  
        except urllib2.URLError, exception:
            self.handle_url_error_exception(page, exception)
        except BadStatusLine, exception:
            self.handle_bad_status_line_exception(page, exception)
        except socket.timeout, exception:
            self.handle_socket_timeout_exception(page, exception)
        except BaseException, exception:
            self.handle_base_exception(page, exception)
            raise

    def handle_url_error_exception(self, page, exception):
        print("URLError exception while processing page: " + page.url)
        print("URLError exception reason: " + str(exception.reason))         
              
    def handle_bad_status_line_exception(self, page, exception):
        print("BadStatusLine exception while processing page: " + page.url)
        print("BadStatusLine exception unknown code status: " + str(exception.message))
        
    def handle_socket_timeout_exception(self, page, exception):
        print("socket.timeout exception while processing page: " + page.url)
        print("socket.timeout exception message: " + str(exception))    

    def handle_base_exception(self, page, exception):
        print("Exception while processing page: " + page.url)
        print("Exception message: " + str(exception))    
        
    def put_extracted_pages_in_queue(self, page):
        extracted_pages = page.extract_pages()
        for page in extracted_pages:
            self.page_queue.put(page) 

    def put_extracted_items_in_queue(self, page):
        extracted_items = page.extract_items()
        for item in extracted_items:
            self.items_queue.put(item)
            
            
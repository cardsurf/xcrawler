
from __future__ import print_function
import time

from .config import Config
from ..threads.work_executor import WorkExecutor


class XCrawler:
    """A multi-threaded web crawler.
    
    Attributes:
        start_pages (list[Page]): the start Pages to be visited by a crawler.
        config (Config): the configuration of a crawler.
    """
    
    def __init__(self, start_pages):
        self.start_pages = start_pages
        self.config = Config()

    def run(self):
        start = time.time()
        if len(self.start_pages) > 0:
            executor = WorkExecutor(self.config)
            executor.execute_work(self.start_pages)
        end = time.time()
        print("Finished scraping. Time elapsed: " + str(end - start))



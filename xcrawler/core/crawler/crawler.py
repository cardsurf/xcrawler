
from __future__ import print_function
import time

from xcrawler.core.crawler.config import ConfigFactory
from xcrawler.threads.work_executor import WorkExecutorFactory


class XCrawler:
    """A multi-threaded web crawler.
    
    Attributes:
        start_pages (list[Page]): the start Pages to be visited by a crawler.
        config (Config): the configuration of a crawler.
    """
    
    def __init__(self,
                 start_pages,
                 config_factory=ConfigFactory(),
                 work_executor_factory=WorkExecutorFactory()):
        self.start_pages = start_pages
        self.config = config_factory.create_config()
        self.work_executor_factory = work_executor_factory

    def run(self):
        start = time.time()
        if len(self.start_pages) > 0:
            executor = self.work_executor_factory.create_work_executor(self.config)
            executor.execute_work(self.start_pages)
        end = time.time()
        print("Finished scraping. Time elapsed: " + str(end - start))



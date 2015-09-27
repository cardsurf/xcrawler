
import time
from config import Config

from ..threads.work_executor import WorkExecutor


class XCrawler(object):
    """A multi-threaded web crawler.
    
    Attributes:
        start_urls (List[str]): the list of urls to be visited by a crawler.
        page_scrapers (List[PageScraper]): the list of page scrapers used to extract data and urls from web pages.
        config (Config): the configuration of a crawler.
    """
    
    def __init__(self, start_urls, page_scrapers):
        self.start_urls = start_urls
        self.page_scrapers = page_scrapers
        self.config = Config()
            
    def run(self):
        self.init_page_scrapers()
        start = time.time()
        if self.get_number_page_scrapers() > 0:
            executor = WorkExecutor(self.config)
            executor.execute_work(self)
          
        end = time.time()
        print "Finished scraping. Time elapsed: " + str(end - start)
        
    def init_page_scrapers(self):
        number_page_scrapers = self.get_number_page_scrapers()
        for i in range(0, number_page_scrapers):
            page_scraper_index = i
            scraper = self.page_scrapers[i]
            scraper.set_crawler_and_index(self, page_scraper_index)
    
    def get_page_scraper(self, index):
        return self.page_scrapers[index]     

    def get_first_page_scraper(self):
        return self.page_scrapers[0]

    def get_number_page_scrapers(self):
        return len(self.page_scrapers)
    
    
    


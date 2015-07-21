
from ..pythonutils import type_utils

class PageScraper():
    """User-defined page scraper which extracts data and urls from a web page.
    
    User defines how to extract data and urls from a web page using methods:
        `extract_items`: defines how to extract data from a web page.
        `extract_urls`: defines how to extract urls for a web page.
    """

    def extract_items(self, page):
        """
        This method is optional.
        In this method user defines how to extract data from a web page.
        :param page: instance of a Page class which contains web page data.
        :returns: list of data objects or a single object.
            These objects should contain data extracted from a web page.
            Example: list of strings, list of custom data objects or single string.
        """
        return []
     
    def extract_urls(self, page):
        """
        This method is optional.
        In this method user defines how to extract urls for a web page.
        A web page may contain urls to other pages, that needs to be visited to extract data.
        Crawler will visit extracted urls one by one.
        :param page: instance of a Page class which contains web page data.
        :returns: list of strings or single string. 
            These strings should be urls to be visited by a crawler. 
        """
        return []

    def set_crawler_and_index(self, crawler, index):
        self.crawler = crawler
        self.index = index

    def extract_items_list(self, page):
        items = self.extract_items(page)
        return type_utils.convert_to_list_if_single_object(items)
    
    def extract_urls_list(self, page):
        urls = self.extract_urls(page)
        return type_utils.convert_to_list_if_single_object(urls)
        
    def get_next_page_scraper_or_none(self):
        if self.is_last_page_scraper():
            return None
        next_page_scraper_index = self.index + 1
        return self.crawler.get_page_scraper(next_page_scraper_index)

    def is_last_page_scraper(self):
        number_page_scrapers = self.crawler.get_number_page_scrapers()
        return self.index == (number_page_scrapers - 1)




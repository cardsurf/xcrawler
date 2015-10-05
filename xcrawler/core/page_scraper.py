
from xcrawler.pythonutils import type_utils


class PageScraper:
    """A user-defined page scraper that extracts data and urls from a web page.
    
    A user defines how to extract data and urls from a web page using the following methods:
        `extract`: returns data extracted from a web page.
        `visit`: returns next Pages to be visited.
    """

    def extract(self, page):
        """
        This method is optional.
        In this method a user defines how to extract data from a web page.
        :param page: the instance of Page that contains web page data.
        :returns: a list of data objects or a single object.
            These objects should contain data extracted from a web page.
            Example: a list of strings, a list of custom data objects or a single string.
        """
        return []
     
    def visit(self, page):
        """
        This method is optional.
        In this method a user defines how to extract urls from a web page.
        A web page may contain urls to other web pages that need to be visited to extract data.
        A Crawler will visit extracted urls one by one.
        :param page: the instance of Page that contains web page data.
        :returns: a list of Pages to be visited by a crawler.
        """
        return []

    def extract_items_list(self, page):
        items = self.extract(page)
        return type_utils.convert_to_list_if_single_object(items)
    
    def extract_pages_list(self, page):
        pages = self.visit(page)
        return type_utils.convert_to_list_if_single_object(pages)




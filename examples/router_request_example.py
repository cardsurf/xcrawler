
from xcrawler import XCrawler, Page, PageScraper


class Scraper(PageScraper):
    def extract(self, page):
        return page.__str__()


start_page = Page("http://192.168.5.5", Scraper())
start_page.request.cookies = {"theme": "classic"}
crawler = XCrawler([start_page])
crawler.config.request_timeout = (5, 5)
crawler.config.output_file_name = "router_request_example_output.csv"
crawler.run()



from xcrawler import XCrawler, Page, PageScraper
from requests.auth import HTTPBasicAuth


class Scraper(PageScraper):
    def extract(self, page):
        return page.__str__()


start_pages = [ Page("http://192.168.1.1/", Scraper()) ]
crawler = XCrawler(start_pages)
crawler.config.output_file_name = "router_session_example_output.csv"
crawler.config.session.headers = {"User-Agent": "Custom User Agent",
                                  "Accept-Language": "fr"}
crawler.config.session.auth = HTTPBasicAuth('admin', 'admin')
crawler.run()

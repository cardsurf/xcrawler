
from xcrawler import XCrawler, Page, PageScraper


class Scraper(PageScraper):
    def extract(self, page):
        topics = page.xpath("//a[@class='question-hyperlink']/text()")
        return topics


start_pages = [ Page("http://stackoverflow.com/questions/16622802/center-image-within-div", Scraper()) ]
crawler = XCrawler(start_pages)
crawler.config.output_file_name = "stackoverflow_example_crawler_output.csv"
crawler.run()



from xcrawler import XCrawler, Page, PageScraper


class Scraper(PageScraper):
    def extract(self, page):
        related_questions = page.xpath("//div[@class='module sidebar-related']//a[@class='question-hyperlink']/text()")
        return related_questions


start_pages = [ Page("http://stackoverflow.com/questions/16622802/center-image-within-div", Scraper()) ]
crawler = XCrawler(start_pages)

crawler.config.output_file_name = "stackoverflow_example_crawler_output.csv"
crawler.config.number_of_threads = 3
crawler.run()



from xcrawler import XCrawler, Page, PageScraper


class WikimediaItem:
    def __init__(self):
        self.name = None
        self.base64 = None


class EncodedScraper(PageScraper):
    def extract(self, page):
        url = page.xpath("//div[@class='fullImageLink']/a/@href")[0]
        item = WikimediaItem()
        item.name = url.split("/")[-1]
        item.base64 = page.file(url)
        return item


start_pages = [ Page("https://commons.wikimedia.org/wiki/File:Records.svg", EncodedScraper()) ]
crawler = XCrawler(start_pages)
crawler.config.output_file_name = "wikimedia_file_example_output.csv"
crawler.run()


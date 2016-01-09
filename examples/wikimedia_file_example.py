
from xcrawler import XCrawler, Page, PageScraper


class WikimediaItem:
    def __init__(self):
        self.name = None
        self.format = None
        self.binary = None


class WikimediaScraper(PageScraper):
    def extract(self, page):
        url = page.xpath("//div[@class='fullImageLink']/a/@href")[0]
        item = WikimediaItem()
        item.name = url.split("/")[-1]
        item.format = url.split(".")[-1]
        item.binary = page.file(url)
        return item


start_pages = [ Page("https://commons.wikimedia.org/wiki/File:Records.svg", WikimediaScraper()) ]
crawler = XCrawler(start_pages)
crawler.config.output_file_name = "wikimedia_file_example_output.csv"
crawler.run()


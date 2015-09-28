
from xcrawler import XCrawler, Page, PageScraper


class WikimediaItem:
    def __init__(self):
        self.title = None
        self.url = None
        self.data = None


class WikimediaPageScraper(PageScraper):
    def extract(self, page):
        titles = page.xpath("//ul[@class='mw-search-results']/li/div[1]/a/@title")
        urls = page.xpath("//ul[@class='mw-search-results']/li/div[1]/a/@href")
        data = page.xpath("//ul[@class='mw-search-results']/li/div[3]/text()")

        items = []
        for i in range(0, len(titles)):
            item = WikimediaItem()
            item.title = titles[i]
            item.url = urls[i]
            item.data = data[i]
            items.append(item)
        return items


start_pages = []
for i in range(1, 6):
    url = "https://commons.wikimedia.org/w/index.php?title=Special:Search&limit=20&offset=" + str(i*20) + "&profile=default&search=water"
    page = Page(url, WikimediaPageScraper())
    start_pages.append(page)

crawler = XCrawler(start_pages)
crawler.config.output_file_name = "wikimedia_search_results_output.csv"
crawler.run()



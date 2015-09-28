
from xcrawler import XCrawler, Page, PageScraper


class WikimediaItem:
    def __init__(self):
        self.title = None
        self.url = None
        self.data = None


class WikimediaPageScraper(PageScraper):
    def extract(self, page):

        '''
        A web page may contain incomplete data.
        An IndexException occurs when trying to access extracted data with an incorrect index.
        try:
           item.title = titles.get[i]
        except IndexError:
           item.title = "ATitleIsMissing!"

        When dealing with incomplete data use the `get` method of the FallbackList class.
        The `get` method returns a fallback value when an IndexException occurs:
            item.title = titles.get(i, fallback="NoTitle")
        '''

        titles = page.xpath("//ul[@class='mw-search-results']/li/div[1]/a/@title")
        urls = page.xpath("//ul[@class='mw-search-results']/li/div[1]/a/@href")
        data = page.xpath("//ul[@class='mw-search-results']/li/div[3]/text()")

        items = []
        for i in range(0, 30):
            item = WikimediaItem()
            item.title = titles.get(i, fallback="NoTitle")
            item.url = urls.get(i, fallback="NoUrl")
            item.data = data.get(i)
            items.append(item)

        return items


start_pages = []
for i in range(1, 3):
    url = "https://commons.wikimedia.org/w/index.php?title=Special:Search&limit=20&offset=" + str(i*20) + "&profile=default&search=water"
    page = Page(url, WikimediaPageScraper())
    start_pages.append(page)

crawler = XCrawler(start_pages)
crawler.config.output_file_name = "wikimedia_fallback_list_output.csv"
crawler.run()


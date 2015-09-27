
import xcrawler


class WikimediaItem(object):
    def __init__(self):
        self.title = None
        self.url = None
        self.data = None
        
class WikimediaPageScraper(xcrawler.PageScraper):
    def extract_items(self, page):
        titles = page.xpath("//ul[@class='mw-search-results']/li/div[1]/a/@title")
        urls = page.xpath("//ul[@class='mw-search-results']/li/div[1]/a/@href")
        data = page.xpath("//ul[@class='mw-search-results']/li/div[3]/text()")

        items = []
        for i in range(0, len(titles)):
            item = WikimediaItem()
            item.title = titles.get(i, fallback="NoTitle")
            item.url = urls.get(i)
            item.data = data.get(i)
            items.append(item)
        return items

start_urls = []
for i in range(1,6):
    start_urls.append("https://commons.wikimedia.org/w/index.php?title=Special:Search&limit=20&offset=" + str(i*20) + "&profile=default&search=water")
page_scrapers = [WikimediaPageScraper()]

crawler = xcrawler.XCrawler(start_urls, page_scrapers)
crawler.config.output_file_name = "wikimedia_search_results_output.csv"

crawler.run()



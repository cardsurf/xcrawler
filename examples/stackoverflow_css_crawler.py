
import xcrawler


class StackOverflowItem(object):
    def __init__(self):
        self.title = None
        self.votes = None
        self.tags = None
        self.url = None

class UrlScraper(xcrawler.PageScraper):
    def extract_urls(self, page):
        relative_urls = page.css_attr(".question-summary h3 a", "href")
        urls = [page.domain_name + relative_url for relative_url in relative_urls]
        return urls

class ItemScraper(xcrawler.PageScraper):
    def extract_items(self, page):
        item = StackOverflowItem()
        item.title = page.css_text("h1 a").get(0, default="NoTitle")
        item.votes = page.css_text(".question .vote-count-post").get(0).strip()
        item.tags = page.css_text(".question .post-tag").get(0)
        item.url = page.url
        return item

start_urls = ["http://stackoverflow.com/questions?sort=votes"]
page_scrapers = [UrlScraper(), ItemScraper()]
crawler = xcrawler.XCrawler(start_urls, page_scrapers)

crawler.config.output_file_name = "stackoverflow_css_crawler_output.csv"
crawler.config.number_of_threads = 3

crawler.run()



from xcrawler import XCrawler, Page, PageScraper


class StackOverflowItem:
    def __init__(self):
        self.title = None
        self.votes = None
        self.tags = None
        self.url = None


class UrlScraper(PageScraper):
    def extract_urls(self, page):
        relative_urls = page.css_attr(".question-summary h3 a", "href")
        return [Page(page.domain_name + relative_url, ItemScraper()) for relative_url in relative_urls]


class ItemScraper(PageScraper):
    def extract_items(self, page):
        item = StackOverflowItem()
        item.title = page.css_text("h1 a")[0]
        item.votes = page.css_text(".question .vote-count-post")[0].strip()
        item.tags = page.css_text(".question .post-tag")[0]
        item.url = page.url
        return item


start_pages = [Page("http://stackoverflow.com/questions?sort=votes", UrlScraper())]
crawler = XCrawler(start_pages)
crawler.config.output_file_name = "stackoverflow_css_crawler_output.csv"
crawler.config.number_of_threads = 3
crawler.run()

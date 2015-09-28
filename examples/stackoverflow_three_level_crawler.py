
from xcrawler import XCrawler, Page, PageScraper


class StackOverflowItem:
    def __init__(self):
        self.url = None
        self.description = None
        self.tag = None
        self.related_tags = None
        self.title = None
        self.votes = None


class TagsScraper(PageScraper):
    def extract_urls(self, page):
        top_three_urls = page.xpath("//a[@class='post-tag']/@href")[0:3]
        return [Page(page.domain_name + url, TagQuestionsScraper()) for url in top_three_urls]


class TagQuestionsScraper(PageScraper):
    def extract_items(self, page):
        item = StackOverflowItem()
        item.description = "A web page with tagged questions"
        item.url = page.url
        item.tag = page.xpath("//div[@class='tagged']/a/text()").get(0)
        item.related_tags = page.xpath("//div[@class='module js-gps-related-tags']//div[not(@*)]/a/text()")
        return item

    def extract_urls(self, page):
        two_latest_urls = page.xpath("//a[@class='question-hyperlink']/@href")[0:2]
        return [Page(page.domain_name + url, QuestionPageScraper()) for url in two_latest_urls]


class QuestionPageScraper(PageScraper):
    def extract_items(self, page):
        item = StackOverflowItem()
        item.description = "A web page with question details"
        item.url = page.url
        item.title = page.css_text("h1 a").get(0)
        item.votes = page.css_text(".question .vote-count-post").get(0).strip()
        return item


start_pages = [Page("http://stackoverflow.com/tags", TagsScraper())]
crawler = XCrawler(start_pages)
crawler.config.output_file_name = "stackoverflow_three_level_scraper.csv"
crawler.config.number_of_threads = 3
crawler.run()


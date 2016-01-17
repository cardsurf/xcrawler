
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
    def visit(self, page):
        hrefs = page.xpath("//a[@class='post-tag']/@href")[0:3]
        urls = page.to_urls(hrefs)
        return [Page(url, TagQuestionsScraper()) for url in urls]


class TagQuestionsScraper(PageScraper):
    def extract(self, page):
        item = StackOverflowItem()
        item.description = "A web page with tagged questions"
        item.url = page.url
        item.tag = page.xpath("//div[@class='tagged']/a/text()").get(0)
        item.related_tags = page.xpath("//div[@class='module js-gps-related-tags']//div[not(@*)]/a/text()")
        return item

    def visit(self, page):
        hrefs = page.xpath("//a[@class='question-hyperlink']/@href")[0:2]
        urls = page.to_urls(hrefs)
        return [Page(url, QuestionScraper()) for url in urls]


class QuestionScraper(PageScraper):
    def extract(self, page):
        item = StackOverflowItem()
        item.description = "A web page with question details"
        item.url = page.url
        item.title = page.css_text("h1 a").get(0)
        item.votes = page.css_text(".question .vote-count-post").get(0).strip()
        return item


start_pages = [ Page("http://stackoverflow.com/tags", TagsScraper()) ]
crawler = XCrawler(start_pages)
crawler.config.output_file_name = "stackoverflow_three_level_crawler_output.csv"
crawler.config.number_of_threads = 3
crawler.run()



from xcrawler import XCrawler, Page, PageScraper


class StackOverflowItem:
    def __init__(self):
        self.title = None
        self.votes = None
        self.tags = None
        self.url = None


class UrlQuestionsScraper(PageScraper):
    def visit(self, page):
        urls = page.css_attr(".question-summary h3 a", "href")
        return [Page(page.domain_name + url, QuestionScraper()) for url in urls]


class QuestionScraper(PageScraper):
    def extract(self, page):
        item = StackOverflowItem()
        item.title = page.css_text("h1 a")[0]
        item.votes = page.css_text(".question .vote-count-post")[0].strip()
        item.tags = page.css_text(".question .post-tag")[0]
        item.url = page.url
        return item


start_pages = [Page("http://stackoverflow.com/questions?sort=votes", UrlQuestionsScraper())]
crawler = XCrawler(start_pages)
crawler.config.output_file_name = "stackoverflow_css_crawler_output.csv"
crawler.config.number_of_threads = 3
crawler.run()

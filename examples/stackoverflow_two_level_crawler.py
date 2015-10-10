
from xcrawler import XCrawler, Page, PageScraper


class StackOverflowItem:
    def __init__(self):
        self.url = None
        self.related_question = None


class QuestionAndUrlsScraper(PageScraper):
    def extract(self, page):
        related_questions = page.xpath("//div[@class='module sidebar-related']//a[@class='question-hyperlink']/text()")
        items = []
        for related_question in related_questions:
            item = StackOverflowItem()
            item.url = page.url
            item.related_question = related_question
            items.append(item)
        return items

    def visit(self, page):
        hrefs = page.xpath("//div[@class='module sidebar-related']//a[@class='question-hyperlink']/@href")
        urls = page.to_urls(hrefs)
        return [Page(url, QuestionsOnlyScraper()) for url in urls]


class QuestionsOnlyScraper(PageScraper):
    def __init__(self):
        super(QuestionsOnlyScraper, self).__init__()
        self.scraper = QuestionAndUrlsScraper()

    def extract(self, page):
        return self.scraper.extract(page)


start_pages = [ Page("http://stackoverflow.com/questions/16622802/center-image-within-div", QuestionAndUrlsScraper()) ]
crawler = XCrawler(start_pages)
crawler.config.output_file_name = "stackoverflow_two_level_crawler_output.csv"
crawler.run()


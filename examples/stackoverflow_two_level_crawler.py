
from xcrawler import XCrawler, Page, PageScraper


class StackOverflowItem:
    def __init__(self):
        self.url = None
        self.related_question = None


class QuestionsUrlsScraper(PageScraper):
    def extract_items(self, page):
        related_questions = page.xpath("//div[@class='module sidebar-related']//a[@class='question-hyperlink']/text()")
        items = []
        for related_question in related_questions:
            item = StackOverflowItem()
            item.url = page.url
            item.related_question = related_question
            items.append(item)
        return items

    def extract_urls(self, page):
        related_urls = page.xpath("//div[@class='module sidebar-related']//a[@class='question-hyperlink']/@href")
        return [Page(page.domain_name + related_url, QuestionsOnlyScraper()) for related_url in related_urls]


class QuestionsOnlyScraper(PageScraper):
    def __init__(self):
        self.items_urls_scraper = QuestionsUrlsScraper()

    def extract_items(self, page):
        return self.items_urls_scraper.extract_items(page)


start_pages = [Page("http://stackoverflow.com/questions/16622802/center-image-within-div", QuestionsUrlsScraper())]
crawler = XCrawler(start_pages)
crawler.config.output_file_name = "stackoverflow_two_level_crawler_output.csv"
crawler.run()


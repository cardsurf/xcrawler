
import xcrawler


class StackOverflowItem(object):
    def __init__(self):
        self.url = None
        self.related_question = None

class FirstLevelPageScraper(xcrawler.PageScraper):
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
        urls = [page.domain_name + related_url for related_url in related_urls]
        return urls 

class SecondLevelPageScraper(xcrawler.PageScraper):
    def __init__(self):
        self.first_level_scraper = FirstLevelPageScraper()
        
    def extract_items(self, page):
        return self.first_level_scraper.extract_items(page)


start_urls = ["http://stackoverflow.com/questions/16622802/center-image-within-div"]
page_scrapers = [FirstLevelPageScraper(), SecondLevelPageScraper()]

crawler = xcrawler.XCrawler(start_urls, page_scrapers)
crawler.config.output_file_name = "stackoverflow_two_level_crawler_output.csv"

crawler.run()



import xcrawler


class StackOverflowItem(object):
    def __init__(self):
        self.url = None
        self.description = None
        self.tag = None
        self.related_tags = None
        self.title = None
        self.votes = None


class FirstLevelScraper(xcrawler.PageScraper):
    def extract_urls(self, page):
        top_three_urls = page.xpath("//a[@class='post-tag']/@href")[0:3]
        top_three_urls = [page.domain_name + url for url in top_three_urls]
        return top_three_urls


class SecondLevelScraper(xcrawler.PageScraper):
    def extract_items(self, page):
        item = StackOverflowItem()
        item.description = "A web page with tagged questions"
        item.url = page.url
        item.tag = page.xpath("//div[@class='tagged']/a/text()").get(0)
        item.related_tags = page.xpath("//div[@class='module js-gps-related-tags']//div[not(@*)]/a/text()")
        return item

    def extract_urls(self, page):
        two_latest_urls = page.xpath("//a[@class='question-hyperlink']/@href")[0:2]
        two_latest_urls = [page.domain_name + url for url in two_latest_urls]
        return two_latest_urls


class ThirdLevelScraper(xcrawler.PageScraper):
    def extract_items(self, page):
        item = StackOverflowItem()
        item.description = "A web page with question details"
        item.url = page.url
        item.title = page.css_text("h1 a").get(0)
        item.votes = page.css_text(".question .vote-count-post").get(0).strip()
        return item


start_urls = ["http://stackoverflow.com/tags"]
page_scrapers = [FirstLevelScraper(), SecondLevelScraper(), ThirdLevelScraper()]

crawler = xcrawler.XCrawler(start_urls, page_scrapers)
crawler.config.output_file_name = "stackoverflow_three_level_scraper.csv"
crawler.config.number_of_threads = 3

crawler.run()




import xcrawler


class Scraper(xcrawler.PageScraper):
    def extract_items(self, page):
        related_questions = page.xpath("//div[@class='module sidebar-related']//a[@class='question-hyperlink']/text()")
        return related_questions

start_urls = ["http://stackoverflow.com/questions/16622802/center-image-within-div"]
page_scrapers = [Scraper()]
crawler = xcrawler.XCrawler(start_urls, page_scrapers)

crawler.config.output_file_name = "stackoverflow_example_crawler_output.csv"
crawler.config.number_of_threads = 3

crawler.run()


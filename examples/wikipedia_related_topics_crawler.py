
from xcrawler import XCrawler, Page, PageScraper


class RelatedTopic:
    def __init__(self):
        self.name = None
        self.url = None


class WikipediaScraper(PageScraper):
    def extract(self, page):
        names = page.xpath("//div[@class='div-col columns column-count column-count-2']/ul[1]/li/a/text()")
        urls = page.xpath("//div[@class='div-col columns column-count column-count-2']/ul[1]/li/a/@href")

        topics = []
        for i in range(0, len(names)):
            topic = RelatedTopic()
            topic.name = names[i]
            topic.url = urls[i]
            topics.append(topic)
        return topics


start_pages = [Page("https://en.wikipedia.org/wiki/Arithmetic", WikipediaScraper())]
crawler = XCrawler(start_pages)
crawler.config.output_file_name = "wikipedia_related_topics_output.csv"
crawler.run()




import xcrawler

class RelatedTopic(object):
    def __init__(self):
        self.name = None
        self.url = None

class WikipediaPageScraper(xcrawler.PageScraper):
    def extract_items(self, page):
        names = page.xpath("//div[@class='div-col columns column-count column-count-2']/ul[1]/li/a/text()")
        urls = page.xpath("//div[@class='div-col columns column-count column-count-2']/ul[1]/li/a/@href")

        topics = []
        for i in range(0, len(names)):
            topic = RelatedTopic()
            topic.name = names[i]
            topic.url = urls[i]
            topics.append(topic)
        return topics

start_urls = ["https://en.wikipedia.org/wiki/Arithmetic"]
page_scrapers = [WikipediaPageScraper()]

crawler = xcrawler.XCrawler(start_urls, page_scrapers)
crawler.config.output_file_name = "wikipedia_related_topics_output.csv"

crawler.run()



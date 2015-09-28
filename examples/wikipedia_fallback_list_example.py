
from xcrawler import XCrawler, Page, PageScraper


class RelatedTopic:
    def __init__(self):
        self.name = None
        self.url = None


class WikipediaScraper(PageScraper):
    def extract(self, page):

        '''
        A web page may contain incomplete data.
        An IndexError occurs when trying to access extracted data with an incorrect index.
        try:
           item.name = names.get[i]
        except IndexError:
           item.name = "ANameIsMissing!"

        When dealing with incomplete data use the `get` method of the FallbackList class.
        The `get` method returns a fallback value when an IndexError occurs:
            item.name = names.get(i, fallback="NoName")
        '''

        names = page.xpath("//div[@class='div-col columns column-count column-count-2']/ul[1]/li/a/text()")
        urls = page.xpath("//div[@class='div-col columns column-count column-count-2']/ul[1]/li/a/@href")

        topics = []
        for i in range(0, 30):
            topic = RelatedTopic()
            topic.name = names.get(i, fallback="NoName")
            topic.url = urls.get(i)
            topics.append(topic)
        return topics


start_pages = [ Page("https://en.wikipedia.org/wiki/Arithmetic", WikipediaScraper()) ]
crawler = XCrawler(start_pages)
crawler.config.output_file_name = "wikipedia_fallback_list_example_output.csv"
crawler.run()



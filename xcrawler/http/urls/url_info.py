
from xcrawler.http.urls.url_splitter import UrlSplitter


class UrlInfo:
    """Gets information about an url.

    """

    def __init__(self,
                 url_splitter=UrlSplitter()):
        self.url_splitter = url_splitter

    def is_relative(self, url):
        domain = self.url_splitter.get_domain(url)
        return len(domain) == 0

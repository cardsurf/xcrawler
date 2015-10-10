
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

from xcrawler.http.urls.url_info import UrlInfo
from xcrawler.http.urls.url_splitter import UrlSplitter


class UrlJoiner:
    """Replaces missing parts of the second url with the parts of the first url.

    """

    def __init__(self,
                 url_info=UrlInfo(),
                 url_splitter=UrlSplitter()):
        self.url_info = url_info
        self.url_splitter = url_splitter

    def join_protocol_domain(self, url1, url2):
        if self.url_info.is_relative(url2):
            protocol_domain = self.url_splitter.get_protocol_domain(url1)
            url2 = self.add_protocol_domain(protocol_domain, url2)
        return url2

    def add_protocol_domain(self, protocol_domain, url):
        url = urljoin(protocol_domain, url)
        return url

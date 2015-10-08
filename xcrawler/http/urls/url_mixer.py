
from xcrawler.http.urls.url_info import UrlInfo
from xcrawler.http.urls.url_joiner import UrlJoiner
from xcrawler.http.urls.url_splitter import UrlSplitter


class UrlMixer:
    """Join parts of the first url with the parts of the second url.

    """

    def __init__(self,
                 url_info=UrlInfo(),
                 url_joiner=UrlJoiner(),
                 url_splitter=UrlSplitter()):
        self.url_info = url_info
        self.url_joiner = url_joiner
        self.url_splitter = url_splitter

    def mix_protocol_domain_list(self, url1, list_urls2):
        urls = []
        for url2 in list_urls2:
            url = self.mix_protocol_domain(url1, url2)
            urls.append(url)
        return urls

    def mix_protocol_domain(self, url1, url2):
        if self.url_info.is_relative(url2):
            url2 = self.prepend_protocol_domain(url1, url2)
        return url2

    def prepend_protocol_domain(self, url1, url2):
        protocol_domain = self.url_splitter.get_protocol_domain(url1)
        url = self.url_joiner.join_protocol_domain_to_url(protocol_domain, url2)
        return url


try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


class UrlJoiner:
    """Joins parts of an url address to an url.

    """

    def join_protocol_domain_list(self, protocol_domain, urls):
        for i, url in enumerate(urls):
            urls[i] = self.join_protocol_domain(protocol_domain, url)
        return urls

    def join_protocol_domain(self, protocol_domain, url):
        url = urljoin(protocol_domain, url)
        return url


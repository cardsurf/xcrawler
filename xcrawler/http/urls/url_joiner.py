
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


class UrlJoiner:
    """Joins parts of an url.

    """

    def join_protocol_domain_to_urls(self, protocol_domain, urls):
        for i, url in enumerate(urls):
            urls[i] = self.join_protocol_domain_to_url(protocol_domain, url)
        return urls

    def join_protocol_domain_to_url(self, protocol_domain, url):
        url = url
        if not url.startswith(protocol_domain):
            url = urljoin(protocol_domain, url)
        return url


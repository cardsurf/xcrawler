
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


class UrlJoiner:
    """Joins parts of an url.

    """

    def join_protocol_domain_to_paths(self, protocol_domain, paths):
        urls = []
        for path in paths:
            url = self.join_protocol_domain_to_path(protocol_domain, path)
            urls.append(url)
        return urls

    def join_protocol_domain_to_path(self, protocol_domain, path):
        url = path
        if not path.startswith(protocol_domain):
            url = urljoin(protocol_domain, path)
        return url


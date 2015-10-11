
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse


class UrlSplitter(object):
    """Splits an url into smaller parts.

    """
    def __init__(self):
        pass

    def parse_url(self, url):
        parsed_url = urlparse(url)
        return parsed_url

    def get_part_url(self, string_pattern, parsed_url):
        part = string_pattern.format(uri=parsed_url)
        return part

    def get_protocol(self, url):
        parsed_url = self.parse_url(url)
        pattern = '{uri.scheme}'
        protocol = self.get_part_url(pattern, parsed_url)
        return protocol

    def get_domain(self, url):
        parsed_url = self.parse_url(url)
        pattern = '{uri.netloc}'
        domain = self.get_part_url(pattern, parsed_url)
        return domain

    def get_protocol_domain(self, url):
        parsed_url = self.parse_url(url)
        pattern = '{uri.scheme}://{uri.netloc}'
        protocol_domain = self.get_part_url(pattern, parsed_url)
        return protocol_domain

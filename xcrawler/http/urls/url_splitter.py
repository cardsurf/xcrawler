
import re
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse


class UrlSplitter:
    """Splits an url into smaller parts.

    """
    def __init__(self):
        self.protocol_domain_separator = "//"
        self.path_separator = "/"

    def parse_url(self, url):
        url = self.format_to_parsable_url(url)
        parsed_url = urlparse(url)
        return parsed_url

    def format_to_parsable_url(self, url):
        if not self.protocol_domain_separator in url:
            url = self.add_protocol_domain_separator(url)
        return url

    def add_protocol_domain_separator(self, url):
        url = url.lstrip(self.path_separator)
        first_part_url = url.split(self.path_separator)[0]
        if self.is_domain(first_part_url):
            url = self.protocol_domain_separator + url
        return url

    def is_domain(self, string):
        is_domain_regex = "^[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}$"
        match = re.match(is_domain_regex, string)
        return match is not None

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

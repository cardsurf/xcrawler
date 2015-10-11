
from xcrawler.http.urls.url_validator import UrlValidator


class UrlFormatter(object):
    """Formats an url string.

    """
    def __init__(self,
                 url_validator=UrlValidator()):
        self.url_validator = url_validator
        self.protocol_domain_separator = "//"
        self.path_separator = "/"

    def format_to_parsable_url(self, url):
        if not self.protocol_domain_separator in url:
            url = self.add_protocol_domain_separator(url)
        return url

    def add_protocol_domain_separator(self, url):
        url = url.lstrip(self.path_separator)
        first_part_url = url.split(self.path_separator)[0]
        if self.url_validator.is_domain(first_part_url):
            url = self.protocol_domain_separator + url
        return url

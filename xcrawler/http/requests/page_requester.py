
try:
    from urllib2 import Request
    from urllib2 import URLError
    from urllib2 import urlopen
    from httplib import BadStatusLine
except ImportError:
    from urllib.request import Request
    from urllib.request import urlopen
    from urllib.error import URLError
    from http.client import BadStatusLine
from lxml.etree import HTMLParser
from lxml.etree import HTML


class PageRequester:
    """Fetches a web page content as an Element object.

    """

    def __init__(self):
        pass

    def fetch(self, url):
        http_header = {'User-Agent': "Urllib Browser"}
        http_request = Request(url, headers=http_header)
        content = self.send_request(http_request)
        return content

    def send_request(self, http_request, request_timeout=5):
        file_content = urlopen(http_request, timeout=request_timeout)
        string_content = file_content.read()
        element_content = self.convert_to_element(string_content)
        return element_content

    def convert_to_element(self, string_content):
        unicode_parser = HTMLParser(encoding="utf-8")
        content_tree = HTML(string_content, parser=unicode_parser)
        return content_tree


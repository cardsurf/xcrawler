
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

from xcrawler.utils.converters.string_converter import StringConverter


class PageRequester:
    """Fetches a web page content as an Element object.

    """

    def __init__(self,
                 string_converter=StringConverter()):
        self.string_converter = string_converter

    def fetch(self, url):
        http_header = {'User-Agent': "Urllib Browser"}
        http_request = Request(url, headers=http_header)
        content = self.send_request(http_request)
        return content

    def send_request(self, http_request, request_timeout=5):
        file_content = urlopen(http_request, timeout=request_timeout)
        string_content = file_content.read()
        element_content = self.string_converter.convert_to_tree_elements(string_content)
        return element_content



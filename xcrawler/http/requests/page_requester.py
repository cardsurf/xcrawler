
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

from xcrawler.utils.converters.string_converter import StringConverter


class PageRequester:
    """Fetches a web page content as an Element object.

    """

    def __init__(self,
                 string_converter=StringConverter()):
        self.string_converter = string_converter

    def send(self, request, request_timeout=5):
        file_content = urlopen(request, timeout=request_timeout)
        string_content = file_content.read()
        element_content = self.string_converter.convert_to_tree_elements(string_content)
        return element_content



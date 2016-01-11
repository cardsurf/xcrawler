
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
import base64

from xcrawler.pythonutils.converters.string_converter import StringConverter


class RequestSender(object):
    """Sends a request to a web server.

    """
    def __init__(self,
                 string_converter=StringConverter()):
        self.string_converter = string_converter

    def get_binary(self, request, request_timeout=5):
        file_content = urlopen(request, timeout=request_timeout)
        string_content = file_content.read()
        return string_content

    def get_base64(self, request, request_timeout=5):
        string_content = self.get_binary(request, request_timeout)
        base64_content = base64.b64encode(string_content)
        return base64_content

    def get_element(self, request, request_timeout=5):
        string_content = self.get_binary(request, request_timeout)
        element_content = self.string_converter.convert_to_tree_elements(string_content)
        return element_content



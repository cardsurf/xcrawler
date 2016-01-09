
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

from xcrawler.pythonutils.converters.string_converter import StringConverter


class RequestSender(object):
    """Sends a request to a web server.

    """
    def __init__(self,
                 string_converter=StringConverter()):
        self.string_converter = string_converter

    def send_binary(self, request, request_timeout=5):
        file_content = urlopen(request, timeout=request_timeout)
        string_content = file_content.read()
        return string_content

    def send(self, request, request_timeout=5):
        file_content = urlopen(request, timeout=request_timeout)
        string_content = file_content.read()
        element_content = self.string_converter.convert_to_tree_elements(string_content)
        return element_content



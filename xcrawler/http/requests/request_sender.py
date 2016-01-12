
from __future__ import print_function
import base64
import socket

try:
    from urllib2 import urlopen
    from urllib2 import URLError
    from httplib import BadStatusLine
except ImportError:
    from urllib.request import urlopen
    from urllib.error import URLError
    from http.client import BadStatusLine

from xcrawler.pythonutils.converters.string_converter import StringConverter


class RequestSender(object):
    """Sends a request to a web server.

    """
    def __init__(self,
                 string_converter=StringConverter()):
        self.string_converter = string_converter

    def get_binary(self, request, request_timeout=5):
        string_content = ""
        try:
            file_content = urlopen(request, timeout=request_timeout)
            string_content = file_content.read()
        except URLError as exception:
            self.handle_url_error_exception(request, exception)
        except BadStatusLine as exception:
            self.handle_bad_status_line_exception(request, exception)
        except socket.timeout as exception:
            self.handle_socket_timeout_exception(request, exception)
        except BaseException as exception:
            self.handle_base_exception(request, exception)
            raise
        return string_content

    def handle_url_error_exception(self, request, exception):
        print("URLError exception while processing page: " + request.url)
        print("URLError exception reason: " + str(exception.reason))

    def handle_bad_status_line_exception(self, request, exception):
        print("BadStatusLine exception while processing page: " + request.url)
        print("BadStatusLine exception unknown code status: " + str(exception.message))

    def handle_socket_timeout_exception(self, request, exception):
        print("socket.timeout exception while processing page: " + request.url)
        print("socket.timeout exception message: " + str(exception))

    def handle_base_exception(self, request, exception):
        print("Exception while processing page: " + request.url)
        print("Exception message: " + str(exception))

    def get_base64(self, request, request_timeout=5):
        string_content = self.get_binary(request, request_timeout)
        base64_content = base64.b64encode(string_content)
        return base64_content

    def get_element(self, request, request_timeout=5):
        string_content = self.get_binary(request, request_timeout)
        element_content = self.string_converter.convert_to_tree_elements(string_content)
        return element_content



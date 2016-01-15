
from __future__ import print_function
from requests import Session, exceptions
import base64

from xcrawler.pythonutils.converters.string_converter import StringConverter


class RequestSender(object):
    """Sends a request to a web server.

    """
    def __init__(self,
                 string_converter=StringConverter(),
                 session=Session(),
                 timeout=(5, 5)):
        self.string_converter = string_converter
        self.session = session
        self.timeout = timeout

    def get_binary(self, request):
        string_content = ""
        try:
            prepared_request = self.session.prepare_request(request)
            response = self.session.send(prepared_request,
                                         stream=self.session.stream,
                                         verify=self.session.verify,
                                         proxies=self.session.proxies,
                                         cert=self.session.cert,
                                         timeout=self.timeout)
            string_content = response.content
        except exceptions.ConnectionError as exception:
            self.handle_request_exception(request, exception)
        except exceptions.HTTPError as exception:
            self.handle_request_exception(request, exception)
        except exceptions.URLRequired as exception:
            self.handle_request_exception(request, exception)
        except exceptions.TooManyRedirects as exception:
            self.handle_request_exception(request, exception)
        except exceptions.Timeout as exception:
            self.handle_request_exception(request, exception)
        except exceptions.RequestException as exception:
            self.handle_request_exception(request, exception)
        except BaseException as exception:
            self.handle_request_exception(request, exception)
            raise
        return string_content

    def handle_request_exception(self, request, exception):
        print("An exception occurred while sending request: " + request.url)
        print(exception.__class__.__name__ + " exception: " + str(exception.message))

    def get_base64(self, request):
        string_content = self.get_binary(request)
        base64_content = base64.b64encode(string_content)
        return base64_content

    def get_element(self, request):
        string_content = self.get_binary(request)
        element_content = self.string_converter.convert_to_tree_elements(string_content)
        return element_content



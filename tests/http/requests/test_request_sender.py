
import unittest
import mock
import socket

from lxml.etree import Element
try:
    from urllib2 import Request
    from urllib2 import urlopen
    from urllib2 import URLError
    from httplib import BadStatusLine
    import __builtin__ as builtins
except ImportError:
    from urllib.request import Request
    from urllib.error import URLError
    from http.client import BadStatusLine
    import builtins

from xcrawler.http.requests.request_sender import RequestSender
from xcrawler.pythonutils.converters.string_converter import StringConverter


class TestRequestSender(unittest.TestCase):

    def setUp(self):
        string_converter = mock.create_autospec(StringConverter).return_value
        self.request_sender = RequestSender(string_converter)

    @mock.patch('xcrawler.http.requests.request_sender.urlopen')
    def test_get_binary(self, mock_urlopen):
        mock_request = mock.create_autospec(Request).return_value
        mock_file_content = mock.Mock()
        mock_string_content = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        mock_urlopen.return_value = mock_file_content
        mock_file_content.read.return_value = mock_string_content
        result = self.request_sender.get_binary(mock_request)
        self.assertEquals(result, mock_string_content)

    @mock.patch('xcrawler.http.requests.request_sender.base64')
    @mock.patch.object(RequestSender, 'get_binary')
    def test_get_base64(self, mock_get_binary, mock_base64):
        mock_request = mock.create_autospec(Request).return_value
        mock_string_content = "<html><a href='url1'>text1</a></html>"
        mock_base64_content = "PGh0bWw+PGEgaHJlZj0ndXJsMSc+dGV4dDE8L2E+PC9odG1sPg=="
        mock_base64.b64encode.return_value = mock_base64_content
        mock_get_binary.return_value = mock_string_content
        result = self.request_sender.get_base64(mock_request)
        self.assertEquals(result, mock_base64_content)

    @mock.patch.object(RequestSender, 'get_binary')
    def test_get_element(self, mock_get_binary):
        mock_request = mock.create_autospec(Request).return_value
        mock_string_content = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        mock_element_content = mock.create_autospec(Element).return_value
        mock_get_binary.return_value = mock_string_content
        self.request_sender.string_converter.convert_to_tree_elements.return_value = mock_element_content
        result = self.request_sender.get_element(mock_request)
        self.assertEquals(result, mock_element_content)

    @mock.patch('tests.http.requests.test_request_sender.builtins.print')
    def test_handle_url_error_exception(self, mock_print_function):
        mock_request = mock.create_autospec(Request).return_value
        mock_request.url = "http://mockurl.mock"
        mock_exception = mock.create_autospec(URLError).return_value
        mock_exception.reason = "UrlError"
        self.request_sender.handle_url_error_exception(mock_request, mock_exception)
        self.assertEquals(mock_print_function.call_count, 2)
     
    @mock.patch('tests.http.requests.test_request_sender.builtins.print')
    def test_handle_bad_status_line_exception(self, mock_print_function):
        mock_request = mock.create_autospec(Request).return_value
        mock_request.url = "http://mockurl.mock"
        mock_exception = mock.create_autospec(BadStatusLine).return_value
        mock_exception.message = "404: not found"
        self.request_sender.handle_bad_status_line_exception(mock_request, mock_exception)
        self.assertEquals(mock_print_function.call_count, 2)
        
    @mock.patch('tests.http.requests.test_request_sender.builtins.print')
    def test_handle_socket_timeout_exception(self, mock_print_function):
        mock_request = mock.create_autospec(Request).return_value
        mock_request.url = "http://mockurl.mock"
        mock_exception = mock.create_autospec(socket.timeout).return_value
        mock_exception.message = "socket timeout"
        self.request_sender.handle_socket_timeout_exception(mock_request, mock_exception)
        self.assertEquals(mock_print_function.call_count, 2)

    @mock.patch('tests.http.requests.test_request_sender.builtins.print')
    def test_handle_base_exception(self, mock_print_function):
        mock_request = mock.create_autospec(Request).return_value
        mock_request.url = "http://mockurl.mock"
        mock_exception = mock.create_autospec(BaseException).return_value
        mock_exception.message = "Base exception message"
        self.request_sender.handle_base_exception(mock_request, mock_exception)
        self.assertEquals(mock_print_function.call_count, 2)

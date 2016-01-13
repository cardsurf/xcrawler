
import unittest
import mock

from requests import Request, Session, Response, exceptions
from lxml.etree import Element
try:
    import __builtin__ as builtins
except ImportError:
    import builtins


from xcrawler.http.requests.request_sender import RequestSender
from xcrawler.pythonutils.converters.string_converter import StringConverter


class TestRequestSender(unittest.TestCase):

    def setUp(self):
        string_converter = mock.create_autospec(StringConverter).return_value
        session = mock.create_autospec(Session).return_value
        self.request_sender = RequestSender(string_converter, session)

    def test_get_binary(self):
        mock_request = mock.create_autospec(Request).return_value
        mock_response = mock.create_autospec(Response).return_value
        mock_response.content = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        self.request_sender.session.send.return_value = mock_response
        result = self.request_sender.get_binary(mock_request)
        self.assertEquals(result, mock_response.content)

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
    def test_handle_exception_connection_error(self, mock_print_function):
        mock_request = mock.create_autospec(Request).return_value
        mock_request.url = "htt;//mockurl.mock"
        mock_exception = mock.create_autospec(exceptions.ConnectionError).return_value
        mock_exception.message = "DNS failure"
        self.request_sender.handle_request_exception(mock_request, mock_exception)
        self.assertEquals(mock_print_function.call_count, 2)

    @mock.patch('tests.http.requests.test_request_sender.builtins.print')
    def test_handle_exception_httperror(self, mock_print_function):
        mock_request = mock.create_autospec(Request).return_value
        mock_request.url = "http://mockurl.mock"
        mock_exception = mock.create_autospec(exceptions.HTTPError).return_value
        mock_exception.message = "Invalid HTTP respons"
        self.request_sender.handle_request_exception(mock_request, mock_exception)
        self.assertEquals(mock_print_function.call_count, 2)

    @mock.patch('tests.http.requests.test_request_sender.builtins.print')
    def test_handle_exception_urlrequired(self, mock_print_function):
        mock_request = mock.create_autospec(Request).return_value
        mock_request.url = "htt;//mockurl.mock"
        mock_exception = mock.create_autospec(exceptions.URLRequired).return_value
        mock_exception.message = "Invalid url"
        self.request_sender.handle_request_exception(mock_request, mock_exception)
        self.assertEquals(mock_print_function.call_count, 2)

    @mock.patch('tests.http.requests.test_request_sender.builtins.print')
    def test_handle_exception_toomanyredirects(self, mock_print_function):
        mock_request = mock.create_autospec(Request).return_value
        mock_request.url = "htt;//mockurl.mock"
        mock_exception = mock.create_autospec(exceptions.TooManyRedirects).return_value
        mock_exception.message = "Number of maximum redirections exceeded"
        self.request_sender.handle_request_exception(mock_request, mock_exception)
        self.assertEquals(mock_print_function.call_count, 2)

    @mock.patch('tests.http.requests.test_request_sender.builtins.print')
    def test_handle_exception_timeout(self, mock_print_function):
        mock_request = mock.create_autospec(Request).return_value
        mock_request.url = "http://mockurl.mock"
        mock_exception = mock.create_autospec(exceptions.Timeout).return_value
        mock_exception.message = "Timeout reached"
        self.request_sender.handle_request_exception(mock_request, mock_exception)
        self.assertEquals(mock_print_function.call_count, 2)

    @mock.patch('tests.http.requests.test_request_sender.builtins.print')
    def test_handle_exception_request_exception(self, mock_print_function):
        mock_request = mock.create_autospec(Request).return_value
        mock_request.url = "http://mockurl.mock"
        mock_exception = mock.create_autospec(exceptions.RequestException).return_value
        mock_exception.message = "RequestException exception message"
        self.request_sender.handle_request_exception(mock_request, mock_exception)
        self.assertEquals(mock_print_function.call_count, 2)

    @mock.patch('tests.http.requests.test_request_sender.builtins.print')
    def test_handle_exception_baseexception(self, mock_print_function):
        mock_request = mock.create_autospec(Request).return_value
        mock_request.url = "http://mockurl.mock"
        mock_exception = mock.create_autospec(BaseException).return_value
        mock_exception.message = "BaseException message"
        self.request_sender.handle_request_exception(mock_request, mock_exception)
        self.assertEquals(mock_print_function.call_count, 2)


import unittest
import mock
from lxml.etree import Element
from lxml.etree import HTMLParser
from lxml.etree import HTML
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


from xcrawler.http.requests.page_requester import PageRequester


class TestPageRequester(unittest.TestCase):

    def setUp(self):
        self.page_requester = PageRequester()

    @mock.patch('xcrawler.http.requests.page_requester.Request')
    @mock.patch.object(PageRequester, 'send_request')
    def test_fetch(self, mock_send_request, mock_request_class):
        mock_url = "http://example.com/path/to/mock_url.html"
        mock_request = mock.create_autospec(Request).return_value
        mock_content = mock.create_autospec(Element).return_value
        mock_request_class.return_value = mock_request
        mock_send_request.return_value = mock_content
        result = self.page_requester.fetch(mock_url)
        self.assertEquals(result, mock_content)

    @mock.patch('xcrawler.http.requests.page_requester.urlopen')
    @mock.patch.object(PageRequester, 'convert_to_element')
    def test_send_request(self, mock_convert_to_element, mock_urlopen):
        mock_request = mock.create_autospec(Request).return_value
        mock_file_content = mock.Mock()
        mock_string_content = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        mock_element_content = mock.create_autospec(Element).return_value
        mock_urlopen.return_value = mock_file_content
        mock_file_content.read.return_value = mock_string_content
        mock_convert_to_element.return_value = mock_element_content
        result = self.page_requester.send_request(mock_request)
        self.assertEquals(result, mock_element_content)

    @mock.patch('xcrawler.http.requests.page_requester.urlopen')
    @mock.patch.object(PageRequester, 'convert_to_element')
    def test_send_request(self, mock_convert_to_element, mock_urlopen):
        mock_request = mock.create_autospec(Request).return_value
        mock_file_content = mock.Mock()
        mock_string_content = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        mock_element_content = mock.create_autospec(Element).return_value
        mock_urlopen.return_value = mock_file_content
        mock_file_content.read.return_value = mock_string_content
        mock_convert_to_element.return_value = mock_element_content
        result = self.page_requester.send_request(mock_request)
        self.assertEquals(result, mock_element_content)

    @mock.patch('xcrawler.http.requests.page_requester.HTMLParser')
    @mock.patch('xcrawler.http.requests.page_requester.HTML')
    def test_convert_to_element(self, mock_html_class, mock_htmlparser_class):
        mock_string_content = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        mock_html_parser = mock.Mock()
        mock_element_content = mock.create_autospec(Element).return_value
        mock_htmlparser_class.return_value = mock_html_parser
        mock_html_class.return_value = mock_element_content
        result = self.page_requester.convert_to_element(mock_string_content)
        self.assertEquals(result, mock_element_content)

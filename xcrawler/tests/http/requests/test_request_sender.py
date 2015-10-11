
import unittest
import mock
from lxml.etree import Element
try:
    from urllib2 import Request
    from urllib2 import urlopen
except ImportError:
    from urllib.request import Request
    from urllib.error import URLError


from xcrawler.http.requests.request_sender import RequestSender
from xcrawler.pythonutils.converters.string_converter import StringConverter


class TestRequestSender(unittest.TestCase):

    def setUp(self):
        string_converter = mock.create_autospec(StringConverter).return_value
        self.request_sender = RequestSender(string_converter)

    @mock.patch('xcrawler.http.requests.request_sender.urlopen')
    def test_send(self, mock_urlopen):
        mock_request = mock.create_autospec(Request).return_value
        mock_file_content = mock.Mock()
        mock_string_content = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        mock_element_content = mock.create_autospec(Element).return_value
        mock_urlopen.return_value = mock_file_content
        mock_file_content.read.return_value = mock_string_content
        self.request_sender.string_converter.convert_to_tree_elements.return_value = mock_element_content
        result = self.request_sender.send(mock_request)
        self.assertEquals(result, mock_element_content)

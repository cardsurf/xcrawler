
import unittest
import mock
try:
    from urlparse import ParseResult
except ImportError:
    from urllib.parse import ParseResult

from xcrawler.http.urls.url_splitter import UrlSplitter


class TestUrlSplitter(unittest.TestCase):

    def setUp(self):
        self.url_splitter = UrlSplitter()

    @mock.patch('xcrawler.http.urls.url_splitter.urlparse')
    def test_parse_url(self, mock_urlparse_function):
        mock_url = "http://test.com/link/to/example_page.html"
        mock_parsed_url = mock.create_autospec(ParseResult).return_value
        mock_urlparse_function.return_value = mock_parsed_url
        result = self.url_splitter.parse_url(mock_url)
        mock_urlparse_function.assert_called_once_with(mock_url)
        self.assertEquals(result, mock_parsed_url)

    def test_part_url(self):
        mock_parsed_url = mock.create_autospec(ParseResult).return_value
        mock_parsed_url.__str__ = "http://test.com/link/to/example_page.html"
        mock_pattern = "{uri.netloc}"
        mock_string_pattern = mock.create_autospec(mock_pattern).return_value
        mock_string_pattern.format.return_value = "test.com"
        result = self.url_splitter.get_part_url(mock_string_pattern, mock_parsed_url)
        mock_string_pattern.format(mock_parsed_url)
        self.assertEquals(result, "test.com")

    @mock.patch.object(UrlSplitter, 'parse_url')
    @mock.patch.object(UrlSplitter, 'get_part_url')
    def test_get_protocol(self, mock_get_part_url, mock_parse_url):
        mock_url = "http://test.com/link/to/example_page.html"
        mock_parse_result = mock.create_autospec(ParseResult).return_value
        mock_parse_url.return_value = mock_parse_result
        mock_get_part_url.return_value = "http"
        result = self.url_splitter.get_protocol(mock_url)
        self.assertEquals(result, "http")

    @mock.patch.object(UrlSplitter, 'parse_url')
    @mock.patch.object(UrlSplitter, 'get_part_url')
    def test_get_protocol(self, mock_get_part_url, mock_parse_url):
        mock_url = "http://test.com/link/to/example_page.html"
        mock_parse_result = mock.create_autospec(ParseResult).return_value
        mock_parse_url.return_value = mock_parse_result
        mock_get_part_url.return_value = "http"
        result = self.url_splitter.get_protocol(mock_url)
        self.assertEquals(result, "http")

    @mock.patch.object(UrlSplitter, 'parse_url')
    @mock.patch.object(UrlSplitter, 'get_part_url')
    def test_get_domain(self, mock_get_part_url, mock_parse_url):
        mock_url = "http://test.com/link/to/example_page.html"
        mock_parse_result = mock.create_autospec(ParseResult).return_value
        mock_parse_url.return_value = mock_parse_result
        mock_get_part_url.return_value = "test.com"
        result = self.url_splitter.get_domain(mock_url)
        self.assertEquals(result, "test.com")

    @mock.patch.object(UrlSplitter, 'parse_url')
    @mock.patch.object(UrlSplitter, 'get_part_url')
    def test_get_protocol_domain(self, mock_get_part_url, mock_parse_url):
        mock_url = "http://test.com/link/to/example_page.html"
        mock_parse_result = mock.create_autospec(ParseResult).return_value
        mock_parse_url.return_value = mock_parse_result
        mock_get_part_url.return_value = "http://test.com/"
        result = self.url_splitter.get_protocol_domain(mock_url)
        self.assertEquals(result, "http://test.com/")



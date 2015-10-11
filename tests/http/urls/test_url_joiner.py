
import unittest
import mock

from xcrawler.http.urls.url_joiner import UrlJoiner
from xcrawler.http.urls.url_splitter import UrlSplitter
from xcrawler.http.urls.url_formatter import UrlFormatter


class TestUrlJoiner(unittest.TestCase):

    def setUp(self):
        url_formatter = mock.create_autospec(UrlFormatter).return_value
        url_splitter = mock.create_autospec(UrlSplitter).return_value
        self.url_joiner = UrlJoiner(url_formatter, url_splitter)

    @mock.patch.object(UrlJoiner, 'add_protocol_domain')
    @mock.patch.object(UrlJoiner, 'format_urls')
    def test_join_protocol_domain(self, mock_format_urls, mock_add_protocol_domain):
        mock_url1 = "http://example.com/path/to/mock_url1.html"
        mock_protocol_domain = "http://example.com"
        mock_url2 = "link/to/example_page.html"
        mock_format_urls.return_value = ["http://example.com/path/to/mock_url1.html", "//link/to/example_page.html"]
        self.url_joiner.url_splitter.get_protocol_domain.return_value = mock_protocol_domain
        mock_add_protocol_domain.return_value = "http://example.com/link/to/example_page.html"
        result = self.url_joiner.join_protocol_domain(mock_url1, mock_url2)
        self.assertEquals(result, "http://example.com/link/to/example_page.html")

    @mock.patch('xcrawler.http.urls.url_joiner.urljoin')
    def test_add_protocol_domain(self, mock_urljoin_function):
        mock_protocol_domain = "http://test.com"
        mock_url = ".link/to/example_page.html"
        mock_urljoin_function.return_value = ["http://test.com/link/to/example_page.html"]
        result = self.url_joiner.add_protocol_domain(mock_protocol_domain, mock_url)
        mock_urljoin_function.assert_called_once_with(mock_protocol_domain, mock_url)
        self.assertEquals(result, mock_urljoin_function.return_value)

    def test_format_urls(self):
        mock_url1 = "/test.com/link/to/example_page.html"
        mock_url2 = "test.com/link/to/example_page.html"
        self.url_joiner.url_formatter.format_to_parsable_url.return_value = "//test.com/link/to/example_page.html"
        result = self.url_joiner.format_urls(mock_url1, mock_url2)
        self.assertEquals(result, ["//test.com/link/to/example_page.html", "//test.com/link/to/example_page.html"])


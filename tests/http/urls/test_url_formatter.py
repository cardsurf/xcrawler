
import unittest
import mock

from xcrawler.http.urls.url_formatter import UrlFormatter
from xcrawler.http.urls.url_validator import UrlValidator


class TestUrlFormatter(unittest.TestCase):

    def setUp(self):
        url_validator = mock.create_autospec(UrlValidator).return_value
        self.url_formatter = UrlFormatter(url_validator)

    @mock.patch.object(UrlFormatter, 'add_protocol_domain_separator')
    def test_format_to_parsable_url(self, mock_add_protocol_domain_separator):
        mock_url = "test.com/link/to/example_page.html"
        mock_add_protocol_domain_separator.return_value = "//test.com/link/to/example_page.html"
        result = self.url_formatter.format_to_parsable_url(mock_url)
        self.assertEquals(result, "//test.com/link/to/example_page.html")

    def test_add_protocol_domain_separator(self):
        mock_url = "test.com/link/to/example_page.html"
        self.url_formatter.url_validator.is_domain.return_value = True
        result = self.url_formatter.add_protocol_domain_separator(mock_url)
        self.assertEquals(result, "//test.com/link/to/example_page.html")

    @mock.patch.object(UrlFormatter, 'format_to_parsable_url')
    def test_list_format_to_parsable_url(self, mock_format_to_parsable_url):
        mock_url1 = "/test.com/link/to/example_page.html"
        mock_url2 = "test.com/link/to/example_page.html"
        mock_urls = [mock_url1, mock_url2]
        mock_format_to_parsable_url.return_value = "//test.com/link/to/example_page.html"
        result = self.url_formatter.list_format_to_parsable_url(mock_urls)
        self.assertEquals(result, ["//test.com/link/to/example_page.html", "//test.com/link/to/example_page.html"])




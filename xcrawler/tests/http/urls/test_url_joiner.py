
import unittest
import mock

from xcrawler.http.urls.url_joiner import UrlJoiner
from xcrawler.http.urls.url_info import UrlInfo
from xcrawler.http.urls.url_splitter import UrlSplitter


class TestUrlJoiner(unittest.TestCase):

    def setUp(self):
        url_info = mock.create_autospec(UrlInfo).return_value
        url_splitter = mock.create_autospec(UrlSplitter).return_value
        self.url_joiner = UrlJoiner(url_info, url_splitter)

    @mock.patch.object(UrlJoiner, 'add_protocol_domain')
    def test_join_protocol_domain(self, mock_add_protocol_domain):
        mock_url1 = "http://example.com/path/to/mock_url1.html"
        mock_protocol_domain = "http://example.com"
        mock_url2 = "link/to/example_page.html"
        self.url_joiner.url_info.is_relative.return_value = True
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

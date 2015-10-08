
import unittest
import mock

from xcrawler.http.urls.url_joiner import UrlJoiner


class TestUrlJoiner(unittest.TestCase):

    def setUp(self):
        self.url_joiner = UrlJoiner()

    @mock.patch.object(UrlJoiner, 'join_protocol_domain')
    def test_join_protocol_domain_list(self, mock_join_protocol_domain):
        mock_protocol_domain = "http://test.com"
        mock_urls = ["http://test.com/link/to/example_page.html", "link/to/example_page.html", "/link/to/example_page.html"]
        mock_join_protocol_domain.return_value = "http://test.com/link/to/example_page.html"
        result = self.url_joiner.join_protocol_domain_list(mock_protocol_domain, mock_urls)
        self.assertEquals(mock_join_protocol_domain.call_count, len(mock_urls))
        self.assertEquals(result, ["http://test.com/link/to/example_page.html", "http://test.com/link/to/example_page.html",
                                   "http://test.com/link/to/example_page.html"])

    @mock.patch('xcrawler.http.urls.url_joiner.urljoin')
    def test_join_protocol_domain(self, mock_urljoin_function):
        mock_protocol_domain = "http://test.com"
        mock_url = ".link/to/example_page.html"
        mock_urljoin_function.return_value = ["http://test.com/link/to/example_page.html"]
        result = self.url_joiner.join_protocol_domain(mock_protocol_domain, mock_url)
        mock_urljoin_function.assert_called_once_with(mock_protocol_domain, mock_url)
        self.assertEquals(result, mock_urljoin_function.return_value)
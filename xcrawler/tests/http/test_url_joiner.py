
import unittest
import mock

from xcrawler.http.urls.url_joiner import UrlJoiner


class TestUrlJoiner(unittest.TestCase):

    def setUp(self):
        self.url_joiner = UrlJoiner()

    @mock.patch.object(UrlJoiner, 'join_protocol_domain_to_path')
    def test_join_protocol_domain_to_paths(self, mock_join_protocol_domain_to_path):
        mock_protocol_domain = "http://test.com"
        mock_paths = ["http://test.com/link/to/example_page.html", "link/to/example_page.html", "/link/to/example_page.html"]
        mock_join_protocol_domain_to_path.return_value = "http://test.com/link/to/example_page.html"
        result = self.url_joiner.join_protocol_domain_to_paths(mock_protocol_domain, mock_paths)
        self.assertEquals(mock_join_protocol_domain_to_path.call_count, len(mock_paths))
        self.assertEquals(result, ["http://test.com/link/to/example_page.html", "http://test.com/link/to/example_page.html",
                                   "http://test.com/link/to/example_page.html"])

    @mock.patch('xcrawler.http.urls.url_joiner.urljoin')
    def test_to_url(self, mock_urljoin_function):
        mock_protocol_domain = "http://test.com"
        mock_path = ".link/to/example_page.html"
        mock_urljoin_function.return_value = ["http://test.com/link/to/example_page.html"]
        result = self.url_joiner.join_protocol_domain_to_path(mock_protocol_domain, mock_path)
        mock_urljoin_function.assert_called_once_with(mock_protocol_domain, mock_path)
        self.assertEquals(result, mock_urljoin_function.return_value)
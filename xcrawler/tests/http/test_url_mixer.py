
import unittest
import mock

from xcrawler.http.urls.url_mixer import UrlMixer
from xcrawler.http.urls.url_joiner import UrlJoiner
from xcrawler.http.urls.url_splitter import UrlSplitter


class TestUrlMixer(unittest.TestCase):

    def setUp(self):
        url_joiner = mock.create_autospec(UrlJoiner).return_value
        url_splitter = mock.create_autospec(UrlSplitter).return_value
        self.url_mixer = UrlMixer(url_joiner, url_splitter)

    @mock.patch.object(UrlMixer, 'mix_protocol_domain_with_path')
    def test_mix_protocol_domain_with_paths_list(self, mock_mix_protocol_domain_with_url):
        mock_url1 = "http://example.com/path/to/mock_url1.html"
        mock_list_urls2 = ["http://test.com/link/to/example_page.html", "link/to/example_page.html", "/link/to/example_page.html"]
        mock_mix_protocol_domain_with_url.return_value = "http://test.com/link/to/example_page.html"
        result = self.url_mixer.mix_protocol_domain_with_paths_list(mock_url1, mock_list_urls2)
        self.assertEquals(mock_mix_protocol_domain_with_url.call_count, len(mock_list_urls2))
        self.assertEquals(result, ["http://test.com/link/to/example_page.html", "http://test.com/link/to/example_page.html",
                                   "http://test.com/link/to/example_page.html"])

    def test_mix_protocol_domain_with_paths(self):
        mock_url1 = "http://example.com/path/to/mock_url1.html"
        mock_url2 = "http://test.com/link/to/example_page.html"
        self.url_mixer.url_splitter.get_protocol_domain.return_value = "http://example.com/"
        self.url_mixer.url_joiner.join_protocol_domain_to_url.return_value = "http://example.com/link/to/example_page.html"
        result = self.url_mixer.mix_protocol_domain_with_path(mock_url1, mock_url2)
        self.assertEquals(result, "http://example.com/link/to/example_page.html")

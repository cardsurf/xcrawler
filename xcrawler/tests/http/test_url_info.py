
import unittest
import mock

from xcrawler.http.urls.url_info import UrlInfo
from xcrawler.http.urls.url_splitter import UrlSplitter


class TestUrlInfo(unittest.TestCase):

    def setUp(self):
        url_splitter = mock.create_autospec(UrlSplitter).return_value
        self.url_info = UrlInfo(url_splitter)

    def test_is_relative_argument_absolute_url(self):
        mock_url = "http://test.com/link/to/example_page.html"
        self.url_info.url_splitter.get_domain.return_value = "test.com"
        result = self.url_info.is_relative(mock_url)
        self.assertEquals(result, True)

    def test_is_relative_argument_relative_url(self):
        mock_url = "/link/to/example_page.html"
        self.url_info.url_splitter.get_domain.return_value = ""
        result = self.url_info.is_relative(mock_url)
        self.assertEquals(result, False)


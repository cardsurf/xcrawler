
import unittest
import mock
try:
    from urllib2 import Request
except ImportError:
    from urllib.request import Request

from xcrawler.http.requests.request_factory import RequestFactory


class TestRequestFactory(unittest.TestCase):

    def setUp(self):
        self.request_factory = RequestFactory()

    @mock.patch('xcrawler.http.requests.request_factory.Request')
    def test_create_request(self, mock_request_class):
        mock_url = "http://example.com/path/to/mock_url.html"
        mock_request = mock.create_autospec(Request).return_value
        mock_request_class.return_value = mock_request
        result = self.request_factory.create_request(mock_url)
        self.assertEquals(result, mock_request)


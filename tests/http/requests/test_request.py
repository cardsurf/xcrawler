
import unittest
import mock

from requests import Request

from xcrawler.http.requests.request import RequestFactory


class TestRequestFactory(unittest.TestCase):

    def setUp(self):
        self.request_factory = RequestFactory()

    @mock.patch('xcrawler.http.requests.request.Request')
    def test_create_request(self, mock_request_class):
        mock_method = "GET"
        mock_url = "http://example.com/path/to/mock_url.html"
        mock_request = mock.create_autospec(Request).return_value
        mock_request_class.return_value = mock_request
        result = self.request_factory.create_request(mock_method, mock_url)
        self.assertEquals(result, mock_request)


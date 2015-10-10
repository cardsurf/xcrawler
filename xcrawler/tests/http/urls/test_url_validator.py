
import unittest
import mock

from xcrawler.http.urls.url_validator import UrlValidator


class TestUrlValidator(unittest.TestCase):

    def setUp(self):
        self.url_validator = UrlValidator()

    @mock.patch('xcrawler.http.urls.url_validator.re.match')
    def test_is_domain_argument_valid_domain(self, mock_match_function):
        mock_domain = "test.com"
        mock_sre_match = mock.Mock()
        mock_match_function.return_value = mock_sre_match
        result = self.url_validator.is_domain(mock_domain)
        self.assertEquals(result, True)

    @mock.patch('xcrawler.http.urls.url_validator.re.match')
    def test_is_domain_argument_invalid_domain(self, mock_match_function):
        mock_domain = "test,com"
        mock_match_function.return_value = None
        result = self.url_validator.is_domain(mock_domain)
        self.assertEquals(result, False)
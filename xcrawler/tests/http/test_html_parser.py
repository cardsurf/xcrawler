import unittest

import mock
from lxml.etree import HTMLParser

from xcrawler.http.parsers.html_parser import HtmlParserFactory


class TestHtmlParser(unittest.TestCase):

    def setUp(self):
        self.html_parser_factory = HtmlParserFactory()

    @mock.patch('xcrawler.http.parsers.html_parser.HTMLParser')
    def test_create_html_parser_unicode(self, mock_html_parser_class):
        mock_html_parser = mock.create_autospec(HTMLParser).return_value
        mock_html_parser_class.return_value = mock_html_parser
        result = self.html_parser_factory.create_html_parser_unicode()
        self.assertEquals(result, mock_html_parser)


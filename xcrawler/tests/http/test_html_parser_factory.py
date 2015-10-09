import unittest

import mock
from lxml.etree import HTMLParser

from xcrawler.http.parsers.html_parser_factory import HtmlParserFactory


class TestHtmlParserFactory(unittest.TestCase):

    def setUp(self):
        self.converter_factory = HtmlParserFactory()

    @mock.patch('xcrawler.http.parsers.html_parser_factory.HTMLParser')
    def test_create_html_parser_unicode(self, mock_html_parser_class):
        mock_html_parser = mock.create_autospec(HTMLParser).return_value
        mock_html_parser_class.return_value = mock_html_parser
        result = self.converter_factory.create_html_parser_unicode()
        self.assertEquals(result, mock_html_parser)


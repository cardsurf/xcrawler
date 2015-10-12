import unittest

import mock
from lxml.etree import Element

from tests.mock import mock_factory
from xcrawler.core.crawler.page import Page
from xcrawler.core.extractor.extractor_factory import ExtractorFactory
from xcrawler.http.requests.request import RequestFactory
from xcrawler.core.extractor.extractor import Extractor
from xcrawler.http.urls.url_joiner import UrlJoiner


class TestPage(unittest.TestCase):

    def setUp(self):
        url = "http://test.com/index1.html"
        scraper = mock_factory.create_mock_page_scraper()
        request_factory = mock.create_autospec(RequestFactory).return_value
        extractor_factory = mock.create_autospec(ExtractorFactory).return_value
        url_joiner = mock.create_autospec(UrlJoiner).return_value
        self.page = Page(url, scraper, request_factory, extractor_factory, url_joiner)
        self.page.content = mock.create_autospec(Element).return_value
        self.page.extractor = mock.create_autospec(Extractor).return_value

    def test_set_content(self):
        mock_content = mock.create_autospec(Element).return_value
        mock_extractor = mock.create_autospec(Extractor).return_value
        self.page.extractor_factory.create_extractor.return_value = mock_extractor
        self.page.content = mock_content
        self.assertEquals(self.page.extractor, mock_extractor)
        
    def test_extract_items(self):
        mock_items_list = mock.Mock()
        self.page.scraper.extract_items_list.return_value = mock_items_list
        items_list = self.page.extract_items()
        self.assertEquals(items_list, mock_items_list)
        
    def test_extract_pages(self):
        mock_pages_list = mock_factory.create_mock_pages(10)
        self.page.scraper.extract_pages_list.return_value = mock_pages_list
        pages_list = self.page.extract_pages()
        self.assertEquals(pages_list, mock_pages_list)

    def test_xpath(self):
        mock_path = "//div[@class='header_blue']"
        self.page.content.__str__ = "<html><div class='header_blue'>text1</div><div class='header_blue'>text2</div></html>"
        self.page.extractor.xpath.return_value = mock_factory.create_mock_fallback_list(["<div>", "<div>"])
        result = self.page.xpath(mock_path)
        self.assertEquals(result, ["<div>", "<div>"])

    def test_css(self):
        mock_path = "a"
        self.page.content.__str__ = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        self.page.extractor.css.return_value = mock_factory.create_mock_fallback_list(["<a>", "<a>"])
        result = self.page.css(mock_path)
        self.assertEquals(result, ["<a>", "<a>"])

    def test_css_text(self):
        mock_path = "a"
        self.page.content.__str__ = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        self.page.extractor.css_text.return_value = mock_factory.create_mock_fallback_list(["text1", "text2"])
        result = self.page.css_text(mock_path)
        self.assertEquals(result, ["text1", "text2"])

    def test_css_attr(self):
        mock_path = "a"
        mock_attribute_name = "href"
        self.page.content.__str__ = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        self.page.extractor.css_attr.return_value = mock_factory.create_mock_fallback_list(["url1", "url2"])
        result = self.page.css_attr(mock_path, mock_attribute_name)
        self.assertEquals(result, ["url1", "url2"])

    @mock.patch.object(Page, 'to_url')
    def test_to_urls(self, mock_to_url):
        self.page.url = "http://test.com/page/url.html"
        links = ["http://test.com/link/to/example_page.html", "link/to/example_page.html", "/link/to/example_page.html"]
        mock_to_url.return_value = "http://test.com/link/to/example_page.html"
        result = self.page.to_urls(links)
        self.assertEquals(mock_to_url.call_count, len(links))
        self.assertEquals(result, ["http://test.com/link/to/example_page.html", "http://test.com/link/to/example_page.html",
                                   "http://test.com/link/to/example_page.html"])

    def test_to_url(self):
        self.page.url = "http://test.com/page/url.html"
        link = "/link/to/example_page.html"
        self.page.url_joiner.join_protocol_domain.return_value = "http://test.com/link/to/example_page.html"
        result = self.page.to_url(link)
        self.page.url_joiner.join_protocol_domain.assert_called_once_with(self.page.url, link)
        self.assertEquals(result, "http://test.com/link/to/example_page.html")

    @mock.patch('xcrawler.core.crawler.page.etree')
    def test_str(self, mock_etree_module):
        mock_etree_module.tostring.return_value = "<html><br>Page title</br></html>"
        result = self.page.__str__()
        self.assertEquals(result, mock_etree_module.tostring.return_value)


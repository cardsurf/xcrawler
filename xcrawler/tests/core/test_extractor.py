
import unittest
import mock
from lxml.etree import Element

from xcrawler.tests.mock import mock_factory
from xcrawler.core.extractor import Extractor
from xcrawler.core.extractor_xpath import ExtractorXPath
from xcrawler.core.extractor_css import ExtractorCss


class TestExtractor(unittest.TestCase):

    def setUp(self):
        root_element = mock.create_autospec(Element).return_value
        extractor_xpath = mock.create_autospec(ExtractorXPath).return_value
        extractor_css = mock.create_autospec(ExtractorCss).return_value
        self.extractor = Extractor(root_element, extractor_xpath, extractor_css)
        
    def test_xpath(self):
        mock_path = "//div[@class='header_blue']"
        self.extractor.root_element.__str__ = "<html><div class='header_blue'>text1</div><div class='header_blue'>text2</div></html>"
        self.extractor.extractor_xpath.xpath.return_value = mock_factory.create_mock_fallback_list(["<div>", "<div>"])
        result = self.extractor.xpath(mock_path)
        self.assertEquals(result, ["<div>", "<div>"])

    def test_css(self):
        mock_path = "a"
        self.extractor.root_element.__str__ = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        self.extractor.extractor_css.css.return_value = mock_factory.create_mock_fallback_list(["<a>", "<a>"])
        result = self.extractor.css(mock_path)
        self.assertEquals(result, ["<a>", "<a>"])

    def test_css_text(self):
        mock_path = "a"
        self.extractor.root_element.__str__ = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        self.extractor.extractor_css.css_text.return_value = mock_factory.create_mock_fallback_list(["text1", "text2"])
        result = self.extractor.css_text(mock_path)
        self.assertEquals(result, ["text1", "text2"])

    def test_css_attr(self):
        mock_path = "a"
        mock_attribute_name = "href"
        self.extractor.root_element.__str__ = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        self.extractor.extractor_css.css_attr.return_value = mock_factory.create_mock_fallback_list(["url1", "url2"])
        result = self.extractor.css_attr(mock_path, mock_attribute_name)
        self.assertEquals(result, ["url1", "url2"])




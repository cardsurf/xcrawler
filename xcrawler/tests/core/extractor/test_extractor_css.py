import unittest

import mock
from lxml.etree import Element
from lxml.cssselect import CSSSelector

from xcrawler.core.extractor.extractor_css import ExtractorCss
from xcrawler.collections.fallback_list import FallbackList
from xcrawler.core.extractor.css_selector import CSSSelectorFactory
from xcrawler.collections.collection_factory import CollectionFactory
from xcrawler.pythonutils.converters.string_converter import StringConverter
from xcrawler.tests.mock import mock_factory


class TestExtractorCss(unittest.TestCase):

    def setUp(self):
        root_element = mock.create_autospec(Element).return_value
        cssselector_factory = mock.create_autospec(CSSSelectorFactory).return_value
        collection_factory = mock.create_autospec(CollectionFactory).return_value
        string_converter = mock.create_autospec(StringConverter).return_value
        self.extractor_css = ExtractorCss(root_element, cssselector_factory, collection_factory, string_converter)

    def test_css(self):
        mock_path = ".sidebar-blue h3 a"
        mock_result_fallback_list = mock.create_autospec(FallbackList).return_value
        mock_result = mock.create_autospec(Element).return_value
        mock_css_selector = mock.create_autospec(CSSSelector).return_value
        mock_call = mock.Mock()
        mock_call.return_value = mock_result
        mock_css_selector.__call__ = mock_call
        self.extractor_css.cssselector_factory.create_css_selector = mock_css_selector
        self.extractor_css.collection_factory.create_fallback_list.return_value = mock_result_fallback_list

        result = self.extractor_css.css(mock_path)
        self.assertEquals(result, mock_result_fallback_list)

    @mock.patch.object(ExtractorCss, 'css')
    @mock.patch.object(ExtractorCss, 'convert_elements_to_text')
    def test_css_text(self, mock_convert_elements_to_text, mock_css):
        mock_root_element = mock.create_autospec(Element).return_value
        mock_root_element.__str__ = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        self.extractor_css.root_element = mock_root_element
        mock_css.return_value = mock_factory.create_mock_fallback_list(["<a>", "<a>"])
        mock_convert_elements_to_text.return_value = mock_factory.create_mock_fallback_list(["text1", "text2"])
        mock_path = "a"
        result = self.extractor_css.css_text(mock_path)
        self.assertEquals(result, ["text1", "text2"])

    @mock.patch('xcrawler.core.extractor.extractor_css.etree')
    def test_convert_elements_to_text(self, mock_etree_module):
        mock_root_element1 = mock.create_autospec(Element).return_value
        mock_root_element1.__str__ = "<a href='url1'>mock_text</a>"
        mock_root_element2 = mock.create_autospec(Element).return_value
        mock_root_element2.__str__ = "<a href='url2'>mock_text</a>"
        mock_list_elements = mock_factory.create_mock_fallback_list([mock_root_element1, mock_root_element2])
        mock_etree_module.tostring.return_value = "mock_text"
        result = self.extractor_css.convert_elements_to_text(mock_list_elements)
        self.assertEquals(result, ["mock_text", "mock_text"])

    @mock.patch.object(ExtractorCss, 'css')
    @mock.patch.object(ExtractorCss, 'convert_elements_to_attribute')
    def test_css_attr(self, mock_convert_elements_to_attribute, mock_css):
        mock_root_element = mock.create_autospec(Element).return_value
        mock_root_element.__str__ = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        self.extractor_css.root_element = mock_root_element
        mock_css.return_value = mock_factory.create_mock_fallback_list(["<a>", "<a>"])
        mock_convert_elements_to_attribute.return_value = mock_factory.create_mock_fallback_list(["url1", "url2"])
        mock_path = "a"
        mock_attribute_name = "href"
        result = self.extractor_css.css_attr(mock_path, mock_attribute_name)
        self.assertEquals(result, ["url1", "url2"])

    def test_convert_elements_to_attribute(self):
        mock_root_element1 = mock.create_autospec(Element).return_value
        mock_root_element1.attrib = {"text": "text1", "href": "url1"}
        mock_root_element2 = mock.create_autospec(Element).return_value
        mock_root_element2.attrib = {"text": "text2", "href": "url2"}
        mock_result = mock_factory.create_mock_fallback_list([mock_root_element1, mock_root_element2])
        mock_attribute_name = "href"
        result = self.extractor_css.convert_elements_to_attribute(mock_result, mock_attribute_name)
        self.assertEquals(result, ["url1", "url2"])
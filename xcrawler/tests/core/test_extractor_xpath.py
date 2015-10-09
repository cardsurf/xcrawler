
import unittest
import mock
from lxml.etree import Element

from xcrawler.core.extractor_xpath import ExtractorXPath
from xcrawler.collections.fallback_list import FallbackList
from xcrawler.utils.factories.collection_factory import CollectionFactory
from xcrawler.utils.converters.string_converter import StringConverter


class TestExtractorXPath(unittest.TestCase):

    def setUp(self):
        root_element = mock.create_autospec(Element).return_value
        collection_factory = mock.create_autospec(CollectionFactory).return_value
        string_converter = mock.create_autospec(StringConverter).return_value
        self.extractor_xpath = ExtractorXPath(root_element, collection_factory, string_converter)

    def test_xpath(self):
        mock_path = "//div[@class='sidebar-blue']//a[@class='question-hyperlink']/text()"
        mock_result_fallback_list = mock.create_autospec(FallbackList).return_value
        mock_result = mock.create_autospec(Element).return_value
        self.extractor_xpath.root_element.xpath.return_value = mock_result
        self.extractor_xpath.collection_factory.create_fallback_list.return_value = mock_result_fallback_list
        result = self.extractor_xpath.xpath(mock_path)
        self.assertEquals(result, mock_result_fallback_list)

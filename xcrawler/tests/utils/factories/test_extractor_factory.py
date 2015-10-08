
import unittest
import mock
from lxml.etree import Element

from xcrawler.utils.factories.extractor_factory import ExtractorFactory


class TestExtractorFactory(unittest.TestCase):

    def setUp(self):
        self.extractor_factory = ExtractorFactory()

    @mock.patch('xcrawler.utils.factories.extractor_factory.ExtractorXPath')
    def test_create_extractor_xpath(self, mock_extractor_xpath_class):
        element = mock.create_autospec(Element).return_value
        self.extractor_factory.create_extractor_xpath(element)
        mock_extractor_xpath_class.assert_called_once_with(element)

    @mock.patch('xcrawler.utils.factories.extractor_factory.ExtractorCss')
    def test_create_extractor_css(self, mock_extractor_css_class):
        element = mock.create_autospec(Element).return_value
        self.extractor_factory.create_extractor_css(element)
        mock_extractor_css_class.assert_called_once_with(element)



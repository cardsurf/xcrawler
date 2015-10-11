import unittest

from lxml.etree import Element
import mock

from xcrawler.core.extractor.extractor_factory import ExtractorFactory
from xcrawler.core.extractor.extractor_xpath import ExtractorXPath
from xcrawler.core.extractor.extractor_css import ExtractorCss


class TestExtractorFactory(unittest.TestCase):

    def setUp(self):
        self.extractor_factory = ExtractorFactory()
        
    @mock.patch.object(ExtractorFactory, 'create_extractor_xpath')
    @mock.patch.object(ExtractorFactory, 'create_extractor_css')
    @mock.patch('xcrawler.core.extractor.extractor_factory.Extractor')
    def test_create_extractor(self, mock_extractor_class, mock_create_extractor_css, mock_create_extractor_xpath):
        mock_element = mock.create_autospec(Element).return_value
        mock_extractor_xpath = mock.create_autospec(ExtractorXPath).return_value
        mock_extractor_css = mock.create_autospec(ExtractorCss).return_value
        mock_create_extractor_xpath.return_value = mock_extractor_xpath
        mock_create_extractor_css.return_value = mock_extractor_css
        self.extractor_factory.create_extractor(mock_element)
        mock_extractor_class.assert_called_once_with(mock_element, mock_extractor_xpath, mock_extractor_css)

    @mock.patch('xcrawler.core.extractor.extractor_factory.ExtractorXPath')
    def test_create_extractor_xpath(self, mock_extractor_xpath_class):
        mock_element = mock.create_autospec(Element).return_value
        self.extractor_factory.create_extractor_xpath(mock_element)
        mock_extractor_xpath_class.assert_called_once_with(mock_element)

    @mock.patch('xcrawler.core.extractor.extractor_factory.ExtractorCss')
    def test_create_extractor_css(self, mock_extractor_css_class):
        mock_element = mock.create_autospec(Element).return_value
        self.extractor_factory.create_extractor_css(mock_element)
        mock_extractor_css_class.assert_called_once_with(mock_element)



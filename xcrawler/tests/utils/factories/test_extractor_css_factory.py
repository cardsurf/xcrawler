
import unittest
import mock
from lxml.etree import Element

from xcrawler.utils.factories.extractor_css_factory import ExtractorCssFactory


class TestExtractorCssFactory(unittest.TestCase):

    def setUp(self):
        self.extractor_css_factory = ExtractorCssFactory()

    @mock.patch('xcrawler.utils.factories.extractor_css_factory.ExtractorCss')
    def test_create_extractor_css(self, mock_extractor_css_class):
        element = mock.create_autospec(Element).return_value
        self.extractor_css_factory.create_extractor_css(element)
        mock_extractor_css_class.assert_called_once_with(element)


import unittest
import mock
from lxml.etree import Element

from xcrawler.core.extractor.element import ElementFactory


class TestCSSSelectorFactory(unittest.TestCase):

    def setUp(self):
        self.element_factory = ElementFactory()

    @mock.patch('xcrawler.core.extractor.element.Element')
    def test_create_element(self, mock_element_class):
        mock_tag = "div"
        mock_element_instance = mock.create_autospec(Element).return_value
        mock_element_class.return_value = mock_element_instance
        self.element_factory.create_element(mock_tag)
        mock_element_class.assert_called_once_with(mock_tag)

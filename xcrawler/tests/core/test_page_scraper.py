
import unittest
import mock

from xcrawler.core.page_scraper import PageScraper
from xcrawler.core.page import Page
from xcrawler.utils.converters.object_converter import ObjectConverter


class TestPageScraper(unittest.TestCase):

    def setUp(self):
        mock_object_converter = mock.create_autospec(ObjectConverter).return_value
        self.page_scraper = PageScraper(mock_object_converter)
        
    def test_extract(self):
        mock_page = mock.create_autospec(Page).return_value
        items = self.page_scraper.extract(mock_page)
        self.assertEquals(items, [])
        
    def test_visit(self):
        mock_page = mock.create_autospec(Page).return_value
        pages = self.page_scraper.visit(mock_page)
        self.assertEquals(pages, [])

    @mock.patch.object(PageScraper, 'extract')
    def test_extract_items_list(self, mock_extract):
        mock_page = mock.create_autospec(Page).return_value
        mock_items = mock.Mock()
        mock_items_list = mock.Mock()
        mock_extract.return_value = mock_items
        self.page_scraper.object_converter.convert_to_list_if_single_object.return_value = mock_items_list
        items_list = self.page_scraper.extract_items_list(mock_page)
        
        mock_extract.assert_called_once_with(mock_page)
        self.assertEquals(items_list, mock_items_list)

    @mock.patch.object(PageScraper, 'visit')
    def test_extract_pages_list(self, mock_visit):
        mock_page = mock.create_autospec(Page).return_value
        mock_pages = mock.Mock()
        mock_pages_list = mock.Mock()
        mock_visit.return_value = mock_pages
        self.page_scraper.object_converter.convert_to_list_if_single_object.return_value = mock_pages_list
        pages_list = self.page_scraper.extract_pages_list(mock_page)
        
        mock_visit.assert_called_once_with(mock_page)
        self.assertEquals(pages_list, mock_pages_list)



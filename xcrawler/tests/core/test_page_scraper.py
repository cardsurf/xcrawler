
import unittest
import mock

import xcrawler
from xcrawler.tests.mock import mock_factory


class TestPageScraper(unittest.TestCase):

    def setUp(self):
        self.page_scraper = xcrawler.PageScraper()
        self.page_scraper.crawler = mock_factory.create_mock_crawler()
        self.page_scraper.index = 0
        
    def test_extract_items(self):
        mock_page = mock.create_autospec(xcrawler.Page).return_value
        items = self.page_scraper.extract_items(mock_page)
        self.assertEquals(items, [])
        
    def test_extract_urls(self):
        mock_page = mock.create_autospec(xcrawler.Page).return_value
        urls = self.page_scraper.extract_urls(mock_page)
        self.assertEquals(urls, [])

    @mock.patch('xcrawler.core.page_scraper.type_utils.convert_to_list_if_single_object')
    @mock.patch.object(xcrawler.PageScraper, 'extract_items')    
    def test_extract_items_list(self, mock_extract_items, mock_convert_to_list_if_single_object_function):
        mock_page = mock.create_autospec(xcrawler.Page).return_value
        mock_items = mock.Mock()
        mock_items_list = mock.Mock()
        mock_extract_items.return_value = mock_items
        mock_convert_to_list_if_single_object_function.return_value = mock_items_list
        items_list = self.page_scraper.extract_items_list(mock_page)
        
        mock_extract_items.assert_called_once_with(mock_page)
        self.assertEquals(items_list, mock_items_list)
        
    @mock.patch('xcrawler.core.page_scraper.type_utils.convert_to_list_if_single_object')
    @mock.patch.object(xcrawler.PageScraper, 'extract_urls')
    def test_extract_pages_list(self, mock_extract_urls, mock_convert_to_list_if_single_object_function):
        mock_page = mock.create_autospec(xcrawler.Page).return_value
        mock_pages = mock.Mock()
        mock_pages_list = mock.Mock()
        mock_extract_urls.return_value = mock_pages
        mock_convert_to_list_if_single_object_function.return_value = mock_pages_list
        pages_list = self.page_scraper.extract_pages_list(mock_page)
        
        mock_extract_urls.assert_called_once_with(mock_page)
        self.assertEquals(pages_list, mock_pages_list)



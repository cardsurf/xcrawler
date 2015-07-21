
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
    def test_extract_urls_list(self, mock_extract_urls, mock_convert_to_list_if_single_object_function):
        mock_page = mock.create_autospec(xcrawler.Page).return_value
        mock_urls = mock.Mock()
        mock_urls_list = mock.Mock()
        mock_extract_urls.return_value = mock_urls
        mock_convert_to_list_if_single_object_function.return_value = mock_urls_list
        urls_list = self.page_scraper.extract_urls_list(mock_page)
        
        mock_extract_urls.assert_called_once_with(mock_page)
        self.assertEquals(urls_list, mock_urls_list)
                
    def test_is_last_page_scraper_true(self):
        self.page_scraper.crawler.get_number_page_scrapers.return_value = 5
        self.page_scraper.index = 4
        is_last = self.page_scraper.is_last_page_scraper()
        self.assertTrue(is_last)
        
    def test_is_last_page_scraper_false(self):
        self.page_scraper.crawler.get_number_page_scrapers.return_value = 5
        self.page_scraper.index = 0
        is_last = self.page_scraper.is_last_page_scraper()
        self.assertFalse(is_last)     
    
    @mock.patch.object(xcrawler.PageScraper, 'is_last_page_scraper')
    def test_get_next_page_scraper_or_none_return_none(self, mock_is_last_page_scraper):
        mock_is_last_page_scraper.return_value = True
        scraper = self.page_scraper.get_next_page_scraper_or_none()
        self.assertEquals(scraper, None)
        
    @mock.patch.object(xcrawler.PageScraper, 'is_last_page_scraper')
    def test_get_next_page_scraper_or_none_return_next_page_scraper(self, mock_is_last_page_scraper):
        mock_is_last_page_scraper.return_value = False
        mock_page_scraper = mock.Mock()
        self.page_scraper.crawler.get_page_scraper.return_value = mock_page_scraper
        scraper = self.page_scraper.get_next_page_scraper_or_none()
        self.assertEquals(scraper, mock_page_scraper)

    
    

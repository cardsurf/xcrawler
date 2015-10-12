import unittest

import mock

from tests.mock import mock_factory
from xcrawler.core.crawler.page_scraper import PageScraper
from xcrawler.core.crawler.page import Page
from xcrawler.pythonutils.converters.object_converter import ObjectConverter


class TestPageScraper(unittest.TestCase):

    def setUp(self):
        object_converter = mock.create_autospec(ObjectConverter).return_value
        self.page_scraper = PageScraper(object_converter)

    def test_extract_return_default(self):
        mock_page = mock.create_autospec(Page).return_value
        items = self.page_scraper.extract(mock_page)
        self.assertEquals(items, [])

    @mock.patch.object(PageScraper, 'extract')
    def test_extract_return_list_items(self, mock_extract):
        mock_page = mock.create_autospec(Page).return_value
        mock_items = mock.Mock()
        mock_items_list = mock.Mock()
        mock_extract.return_value = mock_items
        self.page_scraper.object_converter.convert_to_list_if_single_object.return_value = mock_items_list
        items_list = self.page_scraper.extract_items_list(mock_page)

        mock_extract.assert_called_once_with(mock_page)
        self.assertEquals(items_list, mock_items_list)

    def test_visit_return_default(self):
        mock_page = mock.create_autospec(Page).return_value
        pages = self.page_scraper.visit(mock_page)
        self.assertEquals(pages, [])

    @mock.patch.object(PageScraper, 'visit')
    def test_visit_return_list_pages(self, mock_visit):
        mock_page = mock.create_autospec(Page).return_value
        mock_pages = mock_factory.create_mock_pages(10)
        mock_pages_list = mock.Mock()
        mock_visit.return_value = mock_pages
        self.page_scraper.object_converter.convert_to_list_if_single_object.return_value = mock_pages_list
        pages_list = self.page_scraper.extract_pages_list(mock_page)
        
        mock_visit.assert_called_once_with(mock_page)
        self.assertEquals(pages_list, mock_pages_list)



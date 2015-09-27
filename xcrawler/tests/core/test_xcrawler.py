
import unittest
import mock

import xcrawler
from xcrawler.tests.mock import mock_factory


class TestXCrawler(unittest.TestCase):
    
    def setUp(self):        
        start_urls = ["http://test.com/index1.html", "http://test.com/index2.html", "http://test.com/index3.html"]
        page_scrapers = []
        self.crawler = xcrawler.XCrawler(start_urls, page_scrapers)
  
    def test_init_page_scrapers_with_empty_page_scrapers_list(self):
        self.crawler.page_scrapers = []
        try:
            self.crawler.init_page_scrapers()
        except IndexError:
            self.fail("init_page_scrapers tried to get element from empty list")
         
    def test_init_page_scrapers_with_page_scrapers_list(self):
        number_mock_scrapers = 10
        self.crawler.page_scrapers = mock_factory.create_mock_page_screapers(number_mock_scrapers)
        self.crawler.init_page_scrapers()
        for i in range (0, number_mock_scrapers):
            mock_page_scraper = self.crawler.page_scrapers[i]
            mock_page_scraper.set_crawler_and_index.assert_called_once_with(self.crawler, i)
        
    def test_get_page_scraper_with_invalid_index(self):
        self.crawler.page_scrapers = []
        self.assertRaises(IndexError, self.crawler.get_page_scraper, 0)
        
    def test_get_page_scraper_with_valid_index(self):
        number_mock_scrapers = 10
        self.crawler.page_scrapers = mock_factory.create_mock_page_screapers(number_mock_scrapers)
        for i in range (0, number_mock_scrapers):
            page_scraper = self.crawler.get_page_scraper(i) 
            mock_page_scraper = self.crawler.page_scrapers[i]
            self.assertEquals(page_scraper, mock_page_scraper)
       
    def test_get_first_page_scraper_with_empty_page_scrapers_list(self):
        self.crawler.page_scrapers = []
        self.assertRaises(IndexError, self.crawler.get_first_page_scraper)
  
    def test_get_first_page_scraper_with_page_scrapers_list(self):
        number_mock_scrapers = 10
        self.crawler.page_scrapers = mock_factory.create_mock_page_screapers(number_mock_scrapers)
        page_scraper = self.crawler.get_first_page_scraper()
        self.assertEquals(page_scraper, self.crawler.page_scrapers[0])
  
    def test_get_number_page_scrapers_with_empty_page_scrapers_list(self):
        self.crawler.page_scrapers = []
        number_page_scrapers = self.crawler.get_number_page_scrapers()
        self.assertEquals(number_page_scrapers, 0)
      
    def test_get_number_page_scrapers_with_page_scrapers_list(self):
        number_mock_scrapers = 10
        self.crawler.page_scrapers = mock_factory.create_mock_page_screapers(number_mock_scrapers)
        number_page_scrapers = self.crawler.get_number_page_scrapers()
        self.assertEquals(number_page_scrapers, len(self.crawler.page_scrapers))
            
    @mock.patch('xcrawler.core.xcrawler.WorkExecutor') 
    def test_run_with_empty_page_scrapers_list(self, mock_work_executor_module):
        mock_work_executor_instance = mock_work_executor_module.return_value
        self.crawler.page_scrapers = []
        self.crawler.run()
        self.assertFalse(mock_work_executor_instance.execute_work.called)
        
    @mock.patch('xcrawler.core.xcrawler.WorkExecutor') 
    def test_run_with_page_scrapers_list(self, mock_work_executor_module):
        mock_work_executor_instance = mock_work_executor_module.return_value
        number_mock_scrapers = 10
        self.crawler.page_scrapers = mock_factory.create_mock_page_screapers(number_mock_scrapers)
        self.crawler.run()
        mock_work_executor_instance.execute_work.assert_called_once_with(self.crawler)




import unittest
import mock

from xcrawler.tests.mock import mock_factory
import xcrawler

class TestPage(unittest.TestCase):

    def setUp(self):
        url = "http://test.com/index1.html"
        scraper = mock_factory.create_mock_page_scraper()
        self.page = xcrawler.Page(url, scraper)
        
    @mock.patch('xcrawler.core.page.urlparse')
    def test_get_domain(self, mock_urlparse_module):
        mock_parsed_url = mock.Mock()
        mock_parsed_url.scheme = 'http'
        mock_parsed_url.netloc = 'test.com'
        mock_parsed_url.path ='/index=1.html'
        mock_urlparse_module.return_value = mock_parsed_url
        domain = self.page.domain
        self.assertEquals(domain, "http://test.com")
        
    def test_extract_items(self):
        mock_items_list = mock.Mock()
        self.page.scraper.extract_items_list.return_value = mock_items_list
        items_list = self.page.extract_items()
        self.assertEquals(items_list, mock_items_list)
        
    @mock.patch('xcrawler.core.page.Page')
    def test_extract_pages(self, mock_page_class):
        urls = ["http://test.com/index1.html", "http://test.com/index2.html", "http://test.com/index3.html"]
        self.page.scraper.extract_urls_list.return_value = urls
        self.page.extract_pages()
        number_times_page_constructor_called = mock_page_class.call_count        
        self.assertEquals(number_times_page_constructor_called, len(urls))

    def test_xpath(self):
        mock_page_content = mock.Mock()
        mock_page_content.xpath.return_value = ["mock_result1", "mock_result2", "mock_result3"]
        self.page.content = mock_page_content
        mock_path = '//div[@class="header_blue"])'
        result = self.page.xpath(mock_path)
        self.assertEquals(result,mock_page_content.xpath.return_value) 
  
    @mock.patch.object(xcrawler.Page, 'xpath')
    @mock.patch('xcrawler.core.page.XPathResultExtractor') 
    def test_xpath_index(self, mock_xpath_result_extractor_module, mock_xpath):
        self.page.xpath.return_value = ["mock_result1", "mock_result2", "mock_result3"]
        mock_xpath_result_extractor_module.xpath_result_get_index.return_value = "mock_result2"
        mock_path = '//div[@class="header_blue"])'
        mock_index = 1
        mock_index_error_value = "Unknown"
        result = self.page.xpath_index(mock_path, mock_index, mock_index_error_value)
        self.assertEquals(result, mock_xpath_result_extractor_module.xpath_result_get_index.return_value) 
  
    @mock.patch.object(xcrawler.Page, 'xpath_index')  
    def test_xpath_first(self, mock_xpath_index):
        self.page.xpath_index.return_value = "mock_result1"
        mock_path = '//div[@class="header_blue"])'
        mock_index_error_value = "Unknown"
        result = self.page.xpath_first(mock_path, mock_index_error_value)
        self.assertEquals(result, self.page.xpath_index.return_value)
  
    @mock.patch.object(xcrawler.Page, 'xpath_index')  
    def test_xpath_last(self, mock_xpath_index):
        self.page.xpath_index.return_value = "mock_result3"
        mock_path = '//div[@class="header_blue"])'
        mock_index_error_value = "Unknown"
        result = self.page.xpath_last(mock_path, mock_index_error_value)
        self.assertEquals(result, self.page.xpath_index.return_value)
        
    @mock.patch.object(xcrawler.Page, 'xpath_index')
    @mock.patch('xcrawler.core.page.XPathResultExtractor') 
    def test_xpath_index_strip(self, mock_xpath_result_extractor_module, mock_xpath_index):
        mock_xpath_index.return_value = " mock_result2    "
        mock_xpath_result_extractor_module.xpath_result_strip.return_value = "mock_result2"
        mock_path = '//div[@class="header_blue"])'
        mock_index = 1
        mock_index_error_value = "Unknown"
        mock_strip_pattern = "None"
        result = self.page.xpath_index_strip(mock_path, mock_index, mock_index_error_value, mock_strip_pattern)
        self.assertEquals(result, mock_xpath_result_extractor_module.xpath_result_strip.return_value) 
    
    @mock.patch.object(xcrawler.Page, 'xpath_index_strip')  
    def test_xpath_first_strip(self, mock_xpath_index_strip):
        self.page.xpath_index_strip.return_value = "mock_result1"
        mock_path = '//div[@class="header_blue"])'
        mock_index_error_value = "Unknown"
        mock_strip_pattern = "None"
        result = self.page.xpath_first_strip(mock_path, mock_index_error_value, mock_strip_pattern)
        self.assertEquals(result, self.page.xpath_index_strip.return_value)
  
    @mock.patch.object(xcrawler.Page, 'xpath_index_strip')  
    def test_extract_last_strip(self, mock_xpath_index_strip):
        self.page.xpath_index_strip.return_value = "mock_result3"
        mock_path = '//div[@class="header_blue"])'
        mock_index_error_value = "Unknown"
        mock_strip_pattern = "None"
        result = self.page.xpath_last_strip(mock_path, mock_index_error_value, mock_strip_pattern)
        self.assertEquals(result, self.page.xpath_index_strip.return_value)
        
    @mock.patch('__builtin__.unicode')
    def test_decode_path_to_unicode_object_no_exception(self, mock_unicode_function):
        path = "path"
        unicode_path = "unicode path"
        mock_unicode_function.return_value = unicode_path
        result = self.page.decode_path_to_unicode_object(path)
        self.assertEquals(result, unicode_path)
        
    @mock.patch('__builtin__.unicode')
    @mock.patch('__builtin__.print')
    def test_decode_path_to_unicode_object_exception(self, mock_print_function, mock_unicode_function):
        path = "path"
        unicode_path = "unicode path"
        mock_unicode_function.return_value = unicode_path
        mock_unicode_function.side_effect = ValueError('Boom!')
        result = self.page.decode_path_to_unicode_object(path)
        self.assertEquals(result, path)
        
    @mock.patch('xcrawler.core.page.etree')
    def test_str(self, mock_etree_module):
        mock_etree_module.tostring.return_value = "<html><br>Page title</br></html>"
        result = self.page.__str__()
        self.assertEquals(result, mock_etree_module.tostring.return_value)



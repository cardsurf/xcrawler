
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
    def test_get_domain_name(self, mock_urlparse_module):
        mock_parsed_url = mock.Mock()
        mock_parsed_url.scheme = 'http'
        mock_parsed_url.netloc = 'test.com'
        mock_parsed_url.path ='/index=1.html'
        mock_urlparse_module.return_value = mock_parsed_url
        domain_name = self.page.domain_name
        self.assertEquals(domain_name, "http://test.com")
        
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
        mock_page_content.__str__ = "<html><div class='header_blue'>text1</div><div class='header_blue'>text2</div></html>"
        mock_page_content.xpath.return_value = ["<div>", "<div>"]
        self.page.content = mock_page_content
        mock_path = '//div[@class="header_blue"]'
        result = self.page.xpath(mock_path)
        self.assertEquals(result, mock_page_content.xpath.return_value)

    @mock.patch('xcrawler.core.page.CSSSelector')
    def test_css(self, mock_cssselector_module):
        mock_page_content = mock.Mock()
        mock_page_content.__str__ = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        self.page.content = mock_page_content
        mock_selector = mock.Mock()
        mock_selector.return_value = ["<a>", "<a>"]
        mock_cssselector_module.return_value = mock_selector
        mock_path = "a"
        result = self.page.css(mock_path)
        self.assertEquals(result, mock_selector.return_value)

    @mock.patch.object(xcrawler.Page, 'css')
    @mock.patch.object(xcrawler.Page, 'convert_elements_to_text')
    def test_css_text(self, mock_convert_elements_to_text, mock_css):
        mock_page_content = mock.Mock()
        mock_page_content.__str__ = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        self.page.content = mock_page_content
        mock_css.return_value = ["<a>", "<a>"]
        mock_convert_elements_to_text.return_value = ["text1", "text2"]
        mock_path = "a"
        result = self.page.css_text(mock_path)
        self.assertEquals(result, ["text1", "text2"])

    @mock.patch('xcrawler.core.page.etree')
    def test_convert_elements_to_text(self, mock_etree_module):
        mock_list_elements = ["<a href='url1'>mock_text</a>", "<a href='url2'>mock_text</a>"]
        mock_etree_module.tostring.return_value = "mock_text"
        result = self.page.convert_elements_to_text(mock_list_elements)
        self.assertEquals(result, ["mock_text", "mock_text"])

    @mock.patch.object(xcrawler.Page, 'css')
    @mock.patch.object(xcrawler.Page, 'convert_elements_to_attribute')
    def test_css_attr(self, mock_convert_elements_to_attribute, mock_css):
        mock_page_content = mock.Mock()
        mock_page_content.__str__ = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        self.page.content = mock_page_content
        mock_css.return_value = ["<a>", "<a>"]
        mock_convert_elements_to_attribute.return_value = ["url1", "url2"]
        mock_path = "a"
        mock_attribute_name = "href"
        result = self.page.css_attr(mock_path, mock_attribute_name)
        self.assertEquals(result, ["url1", "url2"])

    def test_convert_elements_to_attribute(self):
        mock_element1 = mock.Mock()
        mock_element1.attrib = {"text": "text1", "href": "url1"}
        mock_element2 = mock.Mock()
        mock_element2.attrib = {"text": "text2", "href": "url2"}
        mock_result = [mock_element1, mock_element2]
        mock_attribute_name = "href"
        result = self.page.convert_elements_to_attribute(mock_result, mock_attribute_name)
        self.assertEquals(result, ["url1", "url2"])

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



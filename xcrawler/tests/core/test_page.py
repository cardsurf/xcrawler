
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
    def test_get_domain_name(self, mock_urlparse_function):
        mock_parsed_url = mock.Mock()
        mock_parsed_url.scheme = 'http'
        mock_parsed_url.netloc = 'test.com'
        mock_parsed_url.path ='/index=1.html'
        mock_urlparse_function.return_value = mock_parsed_url
        domain_name = self.page.domain_name
        self.assertEquals(domain_name, "http://test.com")
        
    def test_extract_items(self):
        mock_items_list = mock.Mock()
        self.page.scraper.extract_items_list.return_value = mock_items_list
        items_list = self.page.extract_items()
        self.assertEquals(items_list, mock_items_list)
        
    @mock.patch('xcrawler.core.page.Page')
    def test_extract_pages(self, mock_page_class):
        mock_pages_list = mock_factory.create_mock_pages(10)
        self.page.scraper.extract_pages_list.return_value = mock_pages_list
        pages_list = self.page.extract_pages()
        self.assertEquals(pages_list, mock_pages_list)

    @mock.patch('xcrawler.core.page.FallbackList')
    def test_xpath(self, mock_fallback_list_module):
        mock_fallback_list_instance = mock_fallback_list_module.return_value
        mock_page_content = mock.Mock()
        mock_page_content.__str__ = "<html><div class='header_blue'>text1</div><div class='header_blue'>text2</div></html>"
        mock_page_content.xpath.return_value = ["<div>", "<div>"]
        self.page.content = mock_page_content
        mock_path = '//div[@class="header_blue"]'
        result = self.page.xpath(mock_path)

        self.assertEquals(result, mock_fallback_list_instance)
        mock_fallback_list_module.assert_called_once_with(mock_page_content.xpath.return_value)

    @mock.patch('xcrawler.core.page.FallbackList')
    @mock.patch('xcrawler.core.page.CSSSelector')
    def test_css(self, mock_cssselector_module, mock_fallback_list_module):
        mock_fallback_list_instance = mock_fallback_list_module.return_value
        mock_page_content = mock.Mock()
        mock_page_content.__str__ = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        self.page.content = mock_page_content
        mock_selector = mock.Mock()
        mock_selector.return_value = ["<a>", "<a>"]
        mock_cssselector_module.return_value = mock_selector
        mock_path = "a"
        result = self.page.css(mock_path)

        self.assertEquals(result, mock_fallback_list_instance)
        mock_fallback_list_module.assert_called_once_with(mock_selector.return_value)

    @mock.patch.object(xcrawler.Page, 'css')
    @mock.patch.object(xcrawler.Page, 'convert_elements_to_text')
    def test_css_text(self, mock_convert_elements_to_text, mock_css):
        mock_page_content = mock.Mock()
        mock_page_content.__str__ = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        self.page.content = mock_page_content
        mock_css.return_value = mock_factory.create_mock_fallback_list(["<a>", "<a>"])
        mock_convert_elements_to_text.return_value = mock_factory.create_mock_fallback_list(["text1", "text2"])
        mock_path = "a"
        result = self.page.css_text(mock_path)
        self.assertEquals(result, ["text1", "text2"])

    @mock.patch('xcrawler.core.page.etree')
    def test_convert_elements_to_text(self, mock_etree_module):
        mock_list_elements = mock_factory.create_mock_fallback_list(["<a href='url1'>mock_text</a>", "<a href='url2'>mock_text</a>"])
        mock_etree_module.tostring.return_value = "mock_text"
        result = self.page.convert_elements_to_text(mock_list_elements)
        self.assertEquals(result, ["mock_text", "mock_text"])

    @mock.patch.object(xcrawler.Page, 'css')
    @mock.patch.object(xcrawler.Page, 'convert_elements_to_attribute')
    def test_css_attr(self, mock_convert_elements_to_attribute, mock_css):
        mock_page_content = mock.Mock()
        mock_page_content.__str__ = "<html><a href='url1'>text1</a><a href='url2'>text2</a></html>"
        self.page.content = mock_page_content
        mock_css.return_value = mock_factory.create_mock_fallback_list(["<a>", "<a>"])
        mock_convert_elements_to_attribute.return_value = mock_factory.create_mock_fallback_list(["url1", "url2"])
        mock_path = "a"
        mock_attribute_name = "href"
        result = self.page.css_attr(mock_path, mock_attribute_name)
        self.assertEquals(result, ["url1", "url2"])

    def test_convert_elements_to_attribute(self):
        mock_element1 = mock.Mock()
        mock_element1.attrib = {"text": "text1", "href": "url1"}
        mock_element2 = mock.Mock()
        mock_element2.attrib = {"text": "text2", "href": "url2"}
        mock_result = mock_factory.create_mock_fallback_list([mock_element1, mock_element2])
        mock_attribute_name = "href"
        result = self.page.convert_elements_to_attribute(mock_result, mock_attribute_name)
        self.assertEquals(result, ["url1", "url2"])

    @mock.patch('xcrawler.core.page.string_utils.convert_string_to_unicode')
    def test_decode_path_to_unicode_object(self, mock_convert_string_to_unicode):
        path = "path"
        unicode_path = "unicode path"
        mock_convert_string_to_unicode.return_value = unicode_path
        result = self.page.decode_path_to_unicode_object(path)
        self.assertEquals(result, unicode_path)

    @mock.patch('builtins.print')
    def test_handle_value_error_exception(self, mock_print_function):
        mock_path = "//div[@class='sidebar-blue']//a[@class='question-hyperlink']/text()"
        mock_exception = mock.Mock()
        mock_exception.message = "ValueError exception message"
        self.page.handle_value_error_exception(mock_path, mock_exception)
        self.assertEquals(mock_print_function.call_count, 2)

    @mock.patch('builtins.print')
    def test_handle_base_exception(self, mock_print_function):
        mock_path = "//div[@class='sidebar-blue']//a[@class='question-hyperlink']/text()"
        mock_exception = mock.Mock()
        mock_exception.message = "Base exception message"
        self.page.handle_base_exception(mock_path, mock_exception)
        self.assertEquals(mock_print_function.call_count, 2)

    @mock.patch.object(xcrawler.Page, 'to_url')
    def test_to_urls(self, mock_to_url):
        self.page.domain_name = "http://test.com"
        links = ["http://test.com/link/to/example_page.html", "link/to/example_page.html", "/link/to/example_page.html"]
        mock_to_url.return_value = "http://test.com/link/to/example_page.html"
        result = self.page.to_urls(links)
        self.assertEquals(mock_to_url.call_count, len(links))
        self.assertEquals(result, ["http://test.com/link/to/example_page.html", "http://test.com/link/to/example_page.html",
                                   "http://test.com/link/to/example_page.html"])

    @mock.patch('xcrawler.core.page.urljoin')
    def test_to_url(self, mock_urljoin_function):
        self.page.domain_name = "http://test.com"
        link = ".link/to/example_page.html"
        mock_urljoin_function.return_value = ["http://test.com/link/to/example_page.html"]
        result = self.page.to_url(link)
        mock_urljoin_function.assert_called_once_with(self.page.domain_name, link)
        self.assertEquals(result, mock_urljoin_function.return_value)

    @mock.patch('xcrawler.core.page.etree')
    def test_str(self, mock_etree_module):
        mock_etree_module.tostring.return_value = "<html><br>Page title</br></html>"
        result = self.page.__str__()
        self.assertEquals(result, mock_etree_module.tostring.return_value)


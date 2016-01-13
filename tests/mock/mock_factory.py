
import mock

from requests import Request

from xcrawler.core.crawler.config import Config
from xcrawler.core.crawler.page import Page
from xcrawler.core.crawler.page_scraper import PageScraper
from xcrawler.core.crawler.crawler import XCrawler
from xcrawler.collections.fallback_list import FallbackList


def create_mock_config():
    mock_config = mock.create_autospec(Config)
    mock_config.output_file_name = "output.csv"
    mock_config.output_mode = Config.OUTPUT_MODE_PRINT
    mock_config.number_of_threads = 3
    mock_config.fetch_delay = 0
    return mock_config


def create_mock_page():
    mock_page = mock.create_autospec(Page)
    mock_page.url = "http://test.com/link/to/example_page.html"
    mock_page.request = mock.create_autospec(Request)
    return mock_page


def create_mock_pages(number_mock_pages):
    mock_pages = []
    for _ in range(0, number_mock_pages):
        mock_pages.append(mock.create_autospec(PageScraper))
    return mock_pages


def create_mock_crawler():
    crawler = mock.create_autospec(XCrawler)
    crawler.start_pages = create_mock_pages(10)
    crawler.domain_name = "http://test.com"
    return crawler


def create_mock_page_scraper():
    mock_scrapers = create_mock_page_scrapers(1)
    return mock_scrapers[0]


def create_mock_page_scrapers(number_mock_scrapers):
    mock_scrapers = []
    for _ in range(0, number_mock_scrapers):
        mock_scrapers.append(mock.create_autospec(PageScraper))
    return mock_scrapers


def create_mock_fallback_list(list_elements):
    mock_fallback_list = MockFallbackList(list_elements)
    return mock_fallback_list


class MockFallbackList(FallbackList):
    def get(self, index, fallback="MockFallback"):
        return super(MockFallbackList, self).get(index, fallback)


def create_mock_object_with_str(string):
    mock_object = mock.Mock()
    mock_str = mock.Mock()
    mock_str.return_value = string
    mock_object.__str__ = mock_str
    return mock_object



from lxml.etree import Element

import xcrawler
import mock


def create_mock_config():
    mock_config = mock.create_autospec(xcrawler.Config)
    mock_config.output_file_name = "output.csv"
    mock_config.output_mode = xcrawler.Config.OUTPUT_MODE_PRINT
    mock_config.number_of_threads = 3
    mock_config.fetch_delay = 0
    mock_config.request_timeout = 5
    return mock_config


def create_mock_page():
    mock_page = mock.create_autospec(xcrawler.Page)
    return mock_page


def create_mock_pages(number_mock_pages):
    mock_pages = []
    for _ in range(0, number_mock_pages):
        mock_pages.append(mock.create_autospec(xcrawler.PageScraper))
    return mock_pages


def create_mock_crawler():
    crawler = mock.create_autospec(xcrawler.XCrawler)
    crawler.start_pages = create_mock_pages(10)
    crawler.domain_name = "http://test.com"
    return crawler


def create_mock_page_scraper():
    mock_scrapers = create_mock_page_scrapers(1)
    return mock_scrapers[0]


def create_mock_page_scrapers(number_mock_scrapers):
    mock_scrapers = []
    for _ in range(0, number_mock_scrapers):
        mock_scrapers.append(mock.create_autospec(xcrawler.PageScraper))
    return mock_scrapers


def create_mock_fallback_list(list_elements):
    mock_fallback_list = MockFallbackList(list_elements)
    return mock_fallback_list


class MockFallbackList(xcrawler.FallbackList):
    def get(self, index, fallback="MockFallback"):
        return super(MockFallbackList, self).get(index, fallback)







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


def create_mock_crawler():
    crawler = mock.create_autospec(xcrawler.XCrawler)
    crawler.start_urls = ["http://test.com/index1.html", "http://test.com/index2.html", "http://test.com/index3.html"]
    crawler.domain_name = "test.com"
    crawler.page_scrapers = create_mock_page_screapers(10)
    return crawler


def create_mock_page_screapers(number_mock_scrapers):
    mock_scrapers = []
    for _ in range(0, number_mock_scrapers):
        mock_scrapers.append(mock.create_autospec(xcrawler.PageScraper))
    return mock_scrapers


def create_mock_page_scraper():
    mock_scrapers = create_mock_page_screapers(1)
    return mock_scrapers[0]

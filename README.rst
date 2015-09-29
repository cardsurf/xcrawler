xcrawler
========
A multi-threaded, open source web crawler

Features
---------
* Use multiple threads to visit web pages
* Extract web page data using XPath expressions or CSS selectors
* Extract urls from a web page and visit extracted urls
* Write extracted data to an output file

Installation
------------
#. Install Python 2.7
#. Install lxml library: ``pip install lxml``
#. Install xcrawler:  ``pip install xcrawler``

Usage
-----
| Data and urls are extracted from a web page by a page scraper.
| To extract data and urls from a web page use the following methods:
| ``extract`` returns data extracted from a web page
| ``visit`` returns next Pages to be visited
| 
| A crawler can be configured before crawling web pages. A user can configure such settings of the crawler as:
* the number of threads used to visit web pages
* the name of an output file
* the request timeout
| To run the crawler call:
| ``crawler.run()``
| 
| Examples how to use xcrawler can be found at: https://github.com/cardsurf/xcrawler/tree/master/examples

XPath Example
-------------
.. code:: python

    from xcrawler import XCrawler, Page, PageScraper


    class Scraper(PageScraper):
        def extract(self, page):
            related_questions = page.xpath("//div[@class='module sidebar-related']//a[@class='question-hyperlink']/text()")
            return related_questions


    start_pages = [ Page("http://stackoverflow.com/questions/16622802/center-image-within-div", Scraper()) ]
    crawler = XCrawler(start_pages)

    crawler.config.output_file_name = "stackoverflow_example_crawler_output.csv"
    crawler.config.number_of_threads = 3
    crawler.run()

CSS Example
-------------
.. code:: python

    from xcrawler import XCrawler, Page, PageScraper


    class StackOverflowItem:
        def __init__(self):
            self.title = None
            self.votes = None
            self.tags = None
            self.url = None


    class UrlsScraper(PageScraper):
        def visit(self, page):
            hrefs = page.css_attr(".question-summary h3 a", "href")
            urls = page.to_urls(hrefs)
            return [Page(url, QuestionScraper()) for url in urls]


    class QuestionScraper(PageScraper):
        def extract(self, page):
            item = StackOverflowItem()
            item.title = page.css_text("h1 a")[0]
            item.votes = page.css_text(".question .vote-count-post")[0].strip()
            item.tags = page.css_text(".question .post-tag")[0]
            item.url = page.url
            return item


    start_pages = [ Page("http://stackoverflow.com/questions?sort=votes", UrlsScraper()) ]
    crawler = XCrawler(start_pages)

    crawler.config.output_file_name = "stackoverflow_css_crawler_output.csv"
    crawler.config.number_of_threads = 3
    crawler.run()

Documentation
--------------
| For more information about xcrawler see the source code and Python Docstrings:
| 
* `xcrawler core <https://github.com/cardsurf/xcrawler/tree/master/xcrawler/core/>`_
* `xcrawler threads <https://github.com/cardsurf/xcrawler/tree/master/xcrawler/threads/>`_
* `xcrawler files <https://github.com/cardsurf/xcrawler/tree/master/xcrawler/files/>`_

The documentation can also be accessed at runtime with Python's built-in ``help`` function:

.. code:: python

    >>> import xcrawler
    >>> help(xcrawler.Config)
        # Information about Config
    >>> help(xcrawler.PageScraper.extract)
        # Information about extract method of PageScraper

Licence
-------
GNU GPL v2.0
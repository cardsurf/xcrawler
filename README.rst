xcrawler
========
A multi-threaded, open source web crawler

Features
---------
* Use multiple threads to visit web pages
* Extract data from visited web pages using XPath expressions
* Extract urls from visited web pages and visit extracted urls
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
| ``extract_items``: defines how to extract data from a web page
| ``extract_urls``: defines how to extract urls from a web page
| 
| A crawler can be configured before crawling web pages. A user can configure such settings of the crawler as:
* the number of threads used to visit web pages
* the name of an output file
* the request timeout
| To run the crawler call:
| ``crawler.run()``

Example
-------
.. code:: python

    import xcrawler

    class Scraper(xcrawler.PageScraper):
        def extract_items(self, page):
            related_questions = page.xpath("//div[@class='module sidebar-related']//a[@class='question-hyperlink']/text()")
            return related_questions

    start_urls = ["http://stackoverflow.com/questions/16622802/center-image-within-div"]
    page_scrapers = [Scraper()]
    crawler = xcrawler.XCrawler(start_urls, page_scrapers)

    crawler.config.output_file_name = "stackoverflow_example_crawler_output.csv"
    crawler.config.number_of_threads = 3

    crawler.run()

For more complex examples visit: https://github.com/cardsurf/xcrawler/tree/master/examples


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
    >>> help(xcrawler.PageScraper.extract_items)
        # Information about extract_items method of PageScraper

Licence
-------
GNU GPL v2.0
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse
from lxml import etree

from xcrawler.http.urls.url_joiner import UrlJoiner


class Page:
    """A representation of a web page.
    
    Attributes:
        url (str): the url of a web page.
        scraper (PageScraper): the PageScraper used to extract data and urls from a web page.
        content (Element): the content of a web page represented as an Element object.
            More information about an Element object: http://effbot.org/zone/element.htm
        extractor_xpath (ExtractorXPath): extracts data from an Element object with XPath expressions.
        extractor_css (ExtractorCss): extracts data from an Element object with CSS selectors.
        url_joiner (UrlJoiner): joins parts of an url
        domain_name (str): The domain name of a web page.
    """
    
    def __init__(self,
                 url,
                 page_scraper,
                 content=None,
                 extractor_xpath=None,
                 extractor_css=None,
                 url_joiner=UrlJoiner()):
        self.url = url   
        self.scraper = page_scraper
        self.content = content
        self.extractor_xpath = extractor_xpath
        self.extractor_css = extractor_css
        self.url_joiner = url_joiner
        self.__domain_name = None

    @property
    def domain_name(self):
        if self.__domain_name == None:
            parsed_uri = urlparse(self.url)
            self.__domain_name = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        return self.__domain_name

    @domain_name.setter
    def domain_name(self, value):
        self.__domain_name = value

    def extract_items(self):
        items = self.scraper.extract_items_list(self)
        return items
     
    def extract_pages(self):
        pages = self.scraper.extract_pages_list(self)
        return pages

    def xpath(self, path):
        """
        :param path: the XPath expression.
        :returns: a FallbackList of web page elements that match the XPath expression.
        """
        result = self.extractor_xpath.xpath(path)
        return result

    def css(self, path):
        """
        :param path: the CSS selector.
        :returns: a FallbackList of web page elements that match the CSS selector.
        """
        result = self.extractor_css.css(path)
        return result

    def css_text(self, path):
        """
        :param path: the CSS selector.
        :returns: a FallbackList containing text of web page elements that match the CSS selector.
        """
        result = self.extractor_css.css_text(path)
        return result

    def css_attr(self, path, attribute_name):
        """
        :param path: the CSS selector.
        :param attribute_name: the attribute name of a web page element.
        :returns: a FallbackList containing attribute values of web page elements that match the CSS selector.
        """
        result = self.extractor_css.css_attr(path, attribute_name)
        return result

    def to_urls(self, links):
        """
        This methods converts relative or absolute links to urls.
        If a link does not start with a domain name of a page then the domain name is prepended to the link.
        :param links: the list of links to web pages.
        :returns: the list of web page urls.
        """
        urls = []
        for link in links:
            url = self.to_url(link)
            urls.append(url)
        return urls

    def to_url(self, link):
        """
        This methods converts relative or absolute link to url.
        If a link does not start with a domain name of a page then the domain name is prepended to the link.
        :param link: link to a web page.
        :returns: a web page url.
        """
        url = self.url_joiner.join_protocol_domain_to_url(self.domain_name, link)
        return url

    def __str__(self):
        return etree.tostring(self.content)


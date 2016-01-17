#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse
from lxml import etree

from xcrawler.http.urls.url_joiner import UrlJoiner
from xcrawler.core.extractor.extractor_factory import ExtractorFactory
from xcrawler.http.requests.request import RequestFactory
from xcrawler.http.requests.request_sender import RequestSender


class Page(object):
    """A representation of a web page.
    
    Attributes:
        url (str): the url of a web page.
        scraper (PageScraper): the PageScraper used to extract data and urls from a web page.
        content (Element): the content of a web page represented as an Element object.
            More information about an Element object: http://effbot.org/zone/element.htm
        extractor (Extractor): extracts data from an Element object.
        request (requests.Request): the request send to a web server to fetch a web page.
    """
    def __init__(self,
                 url,
                 page_scraper,
                 request_factory=RequestFactory(),
                 extractor_factory=ExtractorFactory(),
                 url_joiner=UrlJoiner(),
                 request_sender=RequestSender()):
        self.url = url
        self.scraper = page_scraper
        self._content = None
        self.extractor = None
        self.request_factory = request_factory
        self.request = self.request_factory.create_request('GET', self.url)
        self.extractor_factory = extractor_factory
        self.url_joiner = url_joiner
        self.request_sender = request_sender

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
        self.extractor = self.extractor_factory.create_extractor(self.content)

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
        result = self.extractor.xpath(path)
        return result

    def css(self, path):
        """
        :param path: the CSS selector.
        :returns: a FallbackList of web page elements that match the CSS selector.
        """
        result = self.extractor.css(path)
        return result

    def css_text(self, path):
        """
        :param path: the CSS selector.
        :returns: a FallbackList containing text of web page elements that match the CSS selector.
        """
        result = self.extractor.css_text(path)
        return result

    def css_attr(self, path, attribute_name):
        """
        :param path: the CSS selector.
        :param attribute_name: the attribute name of a web page element.
        :returns: a FallbackList containing attribute values of web page elements that match the CSS selector.
        """
        result = self.extractor.css_attr(path, attribute_name)
        return result

    def file(self, url):
        """
        :param url: the url of a file to download
        :returns: a base64 string that represents the file
        """
        request = self.request_factory.create_request('GET', url)
        file_base64 = self.request_sender.get_base64(request)
        return file_base64

    def to_urls(self, links):
        """
        This methods converts links to absolute urls.
        If a link does not have a protocol or a domain then the protocol or the domain of the page is added to the link.
        :param links: the list of links.
        :returns: a list of urls.
        """
        urls = []
        for link in links:
            url = self.to_url(link)
            urls.append(url)
        return urls

    def to_url(self, link):
        """
        This methods converts a link to an absolute url.
        If a link does not have a protocol or a domain then the protocol or the domain of the page is added to the link.
        :param link: the link.
        :returns: an url.
        """
        url = self.url_joiner.join_protocol_domain(self.url, link)
        return url

    def __str__(self):
        return etree.tostring(self.content)


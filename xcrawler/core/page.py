#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse
from lxml import etree

from xcrawler.http.urls.url_mixer import UrlMixer
from xcrawler.utils.factories.extractor_factory import ExtractorFactory
from xcrawler.http.requests.request_factory import RequestFactory


class Page(object):
    """A representation of a web page.
    
    Attributes:
        url (str): the url of a web page.
        scraper (PageScraper): the PageScraper used to extract data and urls from a web page.
        content (Element): the content of a web page represented as an Element object.
            More information about an Element object: http://effbot.org/zone/element.htm
        extractor (Extractor): extracts data from an Element object.
        request (Request): the request send to a web server.
    """
    
    def __init__(self,
                 url,
                 page_scraper,
                 request_factory=RequestFactory(),
                 extractor_factory=ExtractorFactory(),
                 url_mixer=UrlMixer()):
        self.url = url   
        self.scraper = page_scraper
        self._content = None
        self.extractor = None
        self.request = request_factory.create_request(self.url)
        self.extractor_factory = extractor_factory
        self.url_mixer = url_mixer

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
        url = self.url_mixer.mix_protocol_domain(self.url, link)
        return url

    def __str__(self):
        return etree.tostring(self.content)


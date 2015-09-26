#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from lxml import etree
from urlparse import urlparse

from ..collections.fallback_list import FallbackList


class Page():
    """A representation of a web page.
    
    Attributes:
        url (str): the url of a web page.
        scraper (PageScraper): the PageScraper used to extract data and urls from a web page.
        content (Element): the content of a web page represented as Element object.
            More information about Element object: http://effbot.org/zone/element.htm
        domain (str): The domain name of a web page.
    """
    
    def __init__(self, url, page_scraper, content = None):
        self.url = url   
        self.scraper = page_scraper
        self.content = content
        self.__domain = None

    @property
    def domain(self):
        if self.__domain == None:
            parsed_uri = urlparse(self.url)
            self.__domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        return self.__domain

    def extract_items(self):
        items = self.scraper.extract_items_list(self)
        return items
     
    def extract_pages(self):
        urls = self.scraper.extract_urls_list(self)
        next_page_scraper = self.scraper.get_next_page_scraper_or_none()
        
        pages = []
        for url in urls:
            page = Page(url, next_page_scraper)
            pages.append(page)
        return pages

    def xpath(self, path):
        path = self.decode_path_to_unicode_object(path)
        result = self.content.xpath(path)
        result = FallbackList(result)
        return result

    def decode_path_to_unicode_object(self, path, errors = 'strict'):
        try:
            path = unicode(path, 'utf-8', errors=errors)
        except ValueError, exception:
            print("ValueError exception while decoding path to unicode " + path)
            print("ValueError exception message: " + (str(exception)))
        except BaseException, exception:
            print("Exception while decoding path to unicode " + path)
            print("Exception message: " + str(exception))
            raise
        return path

    def __str__(self):
        return etree.tostring(self.content)



from xcrawler.core.extractor import Extractor
from xcrawler.core.extractor_css import ExtractorCss
from xcrawler.core.extractor_xpath import ExtractorXPath


class ExtractorFactory:
    """Creates an extractor.

    """

    def __init__(self):
        pass

    def create_extractor(self, element):
        extractor_xpath = self.create_extractor_xpath(element)
        extractor_css = self.create_extractor_css(element)
        extractor = Extractor(element, extractor_xpath, extractor_css)
        return extractor

    def create_extractor_xpath(self, element):
        extractor_xpath = ExtractorXPath(element)
        return extractor_xpath

    def create_extractor_css(self, element):
        extractor_css = ExtractorCss(element)
        return extractor_css

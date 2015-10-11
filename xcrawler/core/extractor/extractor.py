

class Extractor(object):
    """Extracts data from an instance of an Element object.

    Attributes:
        root_element (Element): an instance of an Element object that contains nested Elements.
        extractor_xpath (ExtractorXPath): extracts data from an Element object with XPath expressions.
        extractor_css (ExtractorCss): extracts data from an Element object with CSS selectors.
    """
    def __init__(self,
                 root_element=None,
                 extractor_xpath=None,
                 extractor_css=None):
        self.root_element = root_element
        self.extractor_xpath = extractor_xpath
        self.extractor_css = extractor_css

    def xpath(self, path):
        result = self.extractor_xpath.xpath(path)
        return result

    def css(self, path):
        result = self.extractor_css.css(path)
        return result

    def css_text(self, path):
        result = self.extractor_css.css_text(path)
        return result

    def css_attr(self, path, attribute_name):
        result = self.extractor_css.css_attr(path, attribute_name)
        return result

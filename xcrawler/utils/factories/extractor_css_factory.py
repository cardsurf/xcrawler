
from xcrawler.core.extractor_css import ExtractorCss


class ExtractorCssFactory:
    """Creates an instance of the ExtractorCss class.

    """

    def __init__(self):
        pass

    def create_extractor_css(self, element):
        extractor_css = ExtractorCss(element)
        return extractor_css


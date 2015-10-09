
from lxml.cssselect import CSSSelector


class CSSSelectorFactory:
    """Creates an instance of the CSSSelector class.

    """
    def __init__(self):
        pass

    def create_css_selector(self, path):
        css_selector = CSSSelector(path)
        return css_selector


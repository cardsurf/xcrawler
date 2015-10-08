
from lxml.cssselect import CSSSelector

from xcrawler.core.selector_css import SelectorCss


class SelectorCssFactory:
    """Creates an instance of the SelectorCss class.

    """

    def __init__(self):
        pass

    def create_selector_css(self, element):
        selector = CSSSelector(element)
        selector_css = SelectorCss(selector)
        return selector_css


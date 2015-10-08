
from xcrawler.core.selector_css import SelectorCss


class SelectorCssFactory:
    """Creates an instance of the SelectorCss class.

    """

    def __init__(self):
        pass

    def create_selector_css(self, element):
        selector_css = SelectorCss(element)
        return selector_css


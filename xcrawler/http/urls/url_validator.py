
import re


class UrlValidator:
    """Validates if a string is a valid part of an url.

    """
    def __init__(self):
        pass

    def is_domain(self, string):
        is_domain_regex = "^[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}$"
        match = re.match(is_domain_regex, string)
        return match is not None
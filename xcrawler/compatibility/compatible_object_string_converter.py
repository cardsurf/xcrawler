
from xcrawler.pythonutils import version_utils
from xcrawler.pythonutils import string_utils


class CompatibleObjectStringConverter:
    """A Python 2 and 3 compatible class for converting an object to a string.

    """
    def __init__(self):
        self.list_convert_to_string = self.get_list_convert_to_string()

    def get_list_convert_to_string(self):
        if version_utils.is_python2():
            return string_utils.list_convert_to_byte_string_utf8
        else:
            return string_utils.list_convert_to_unicode_string


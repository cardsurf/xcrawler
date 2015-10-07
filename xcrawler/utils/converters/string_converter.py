
from xcrawler.utils import string_utils


class StringConverter:
    """Converts a string to a specified type.

    """

    def __init__(self):
        pass

    def convert_to_byte_string_utf8(self, string):
        unicode_string = self.convert_to_unicode_string(string)
        byte_string_utf8 = unicode_string.encode("utf-8")
        return byte_string_utf8

    def convert_to_unicode_string(self, string):
        if string_utils.is_unicode_string(string):
            return string
        unicode_string = string.decode('utf8')
        return unicode_string

    def list_convert_to_unicode_string(self, list_strings):
        return [self.convert_to_unicode_string(s) for s in list_strings]

    def list_convert_to_byte_string_utf8(self, list_strings):
        return [self.convert_to_byte_string_utf8(s) for s in list_strings]


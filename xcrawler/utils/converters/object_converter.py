
from xcrawler.utils import string_utils

class ObjectConverter:
    """Converts an instance of object to specified type.

    """

    def __init__(self):
        pass

    def convert_to_byte_string_utf8(self, o):
        o = self.convert_to_string(o)
        return string_utils.convert_string_to_byte_string_utf8(o)

    def convert_to_unicode_string(self, o):
        o = self.convert_to_string(o)
        return string_utils.convert_string_to_unicode_string(o)

    def convert_to_string(self, o):
        if not string_utils.is_byte_string(o):
            o = str(o)
        return o





from six import string_types, binary_type, text_type


class InstanceResolver:
    """Tests if an object is an instance of a specified type.

    """
    def is_string(self, o):
        return isinstance(o, string_types)

    def is_byte_string(self, o):
        return isinstance(o, binary_type)

    def is_unicode_string(self, o):
        return isinstance(o, text_type)


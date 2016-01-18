
from six import string_types, binary_type, text_type


class InstanceResolver(object):
    """Determines if an object is an instance of a specified type.

    """
    def is_unicode_or_byte_string(self, o):
        return self.is_unicode_string(o) or self.is_byte_string(o)

    def is_unicode_string(self, o):
        return isinstance(o, text_type)

    def is_byte_string(self, o):
        return isinstance(o, binary_type)

    def is_string_python_version(self, o):
        return isinstance(o, string_types)


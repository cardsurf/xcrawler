
from six import string_types, binary_type, text_type


def is_string(o):
    return isinstance(o, string_types)


def is_byte_string(o):
    return isinstance(o, binary_type)


def is_unicode_string(o):
    return isinstance(o, text_type)


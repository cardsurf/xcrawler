
from six import string_types, binary_type, text_type


def is_string(o):
    return isinstance(o, string_types)


def is_byte_string(o):
    return isinstance(o, binary_type)


def is_unicode_string(o):
    return isinstance(o, text_type)


def replace_none_with_empty_string(o):
    if o is None:
        o = ""
    return o


def list_replace_none_with_empty_string(list_objects):
    return [replace_none_with_empty_string(e) for e in list_objects]


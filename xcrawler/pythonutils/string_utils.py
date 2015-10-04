
from six import string_types, binary_type, text_type


def is_string(o):
    return isinstance(o, string_types)


def is_byte_string(o):
    return isinstance(o, binary_type)


def is_unicode_string(o):
    return isinstance(o, text_type)


def convert_to_byte_string_utf8(o):
    o = convert_object_to_string(o)
    return convert_string_to_byte_string_utf8(o)


def convert_to_unicode_string(o):
    o = convert_object_to_string(o)
    return convert_string_to_unicode_string(o)


def convert_object_to_string(o):
    if not is_byte_string(o):
        o = str(o)
    return o


def convert_string_to_unicode_string(string):
    if is_unicode_string(string):
        return string
    unicode_string = string.decode('utf8')
    return unicode_string


def convert_string_to_byte_string_utf8(string):
    unicode_string = convert_string_to_unicode_string(string)
    byte_string_utf8 = unicode_string.encode("utf-8")
    return byte_string_utf8


def replace_none_with_empty_string(o):
    if o is None:
        o = ""
    return o


def list_convert_object_to_string(list_objects):
    return [convert_object_to_string(o) for o in list_objects]


def list_convert_string_to_unicode_string(string_list):
    return [convert_string_to_unicode_string(s) for s in string_list]


def list_convert_string_to_byte_string_utf8(string_list):
    return [convert_string_to_byte_string_utf8(s) for s in string_list]


def list_replace_none_with_empty_string(list_elements):
    return [replace_none_with_empty_string(e) for e in list_elements]


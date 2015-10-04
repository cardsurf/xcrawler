
from six import binary_type, text_type


def is_string(o):
    return isinstance(o, binary_type)


def is_unicode(o):
    return isinstance(o, text_type)


def convert_string_to_unicode(string):
    if is_unicode(string):
        return string
    unicode_object = string.decode('utf8')
    return unicode_object


def convert_string_to_utf8(string):
    unicode_object = convert_string_to_unicode(string)
    byte_string_utf8 = unicode_object.encode("utf-8")
    return byte_string_utf8


def replace_none_with_empty_string(o):
    if o is None:
        o = ""
    return o


def list_convert_object_to_string(list_objects):
    for i, o in enumerate(list_objects):
        if not is_string(o):
            list_objects[i] = str(o)
    return list_objects


def list_convert_string_to_unicode(string_list):
    return [convert_string_to_unicode(s) for s in string_list]


def list_convert_string_to_utf8(string_list):
    return [convert_string_to_utf8(s) for s in string_list]


def list_replace_none_with_empty_string(list_elements):
    return [replace_none_with_empty_string(e) for e in list_elements]


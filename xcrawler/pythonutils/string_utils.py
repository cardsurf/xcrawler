


def is_string(o):
    return isinstance(o, basestring)

def is_unicode(o):
    return isinstance(o, unicode)

def convert_string_to_unicode(string):
    if is_unicode(string):
        return string
    unicode_object = string.decode('utf8')
    return unicode_object

def convert_string_to_utf8(string):
    unicode_object = string
    if not is_unicode(string):
        unicode_object = string.decode('utf8')

    byte_string_utf8 = unicode_object.encode("utf-8")
    return byte_string_utf8

def replace_none_with_empty_string(o):
    if o is None:
        o = ""
    return o

def list_convert_string_to_unicode(string_list):
    return [convert_string_to_unicode(s) for s in string_list]

def list_convert_string_to_utf8(string_list):
    return [convert_string_to_utf8(s) for s in string_list]

def list_replace_none_with_empty_string(list_elements):
    return [replace_none_with_empty_string(e) for e in list_elements]


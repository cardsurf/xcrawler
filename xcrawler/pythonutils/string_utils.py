

def is_string(o):
    return isinstance(o, basestring)
    
def convert_string_to_unicode(string):
    return unicode(string).encode("utf-8")

def replace_none_with_empty_string(o):
    if o is None:
        o = ""
    return o

def list_replace_none_with_empty_string(list_elements):
    for element in list_elements:
        element = replace_none_with_empty_string(element)
    return list_elements

def list_convert_string_to_unicode(string_list):
    return [convert_string_to_unicode(s) for s in string_list]


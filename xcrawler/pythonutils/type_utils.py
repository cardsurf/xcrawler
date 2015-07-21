
def convert_to_list_if_single_object(o):
    if type(o) is not list:
        return [o]
    return o
    
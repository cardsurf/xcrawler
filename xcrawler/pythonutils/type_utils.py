
def convert_to_list_if_single_object(o):
    if isinstance(o, list):
        return o
    return [o]


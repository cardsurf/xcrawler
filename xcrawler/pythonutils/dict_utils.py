

def get_list_of_values_sorted_by_keys(dictionary):
    values = []
    for key in sorted(dictionary): 
        values.append(dictionary[key])
        
    return values

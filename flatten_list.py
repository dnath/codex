def flatten(item_list):
    flattened_list = []
    for item in item_list:
        if type(item) == type([]):
            flattened_list.extend(flatten(item))
        else:
            flattened_list.append(item)
    return flattened_list

print flatten([])
print flatten([1, 2, 3, 4])
print flatten([1, [2, 3], [], 4, [5, [6, [7 ,8 ]]]])

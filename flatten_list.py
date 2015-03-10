def flatten(item_list):
    l = []
    for item in item_list:
        if type(item) == type([]):
            l.extend(flatten(item))
        else:
            l.append(item)
    return l

print flatten([])
print flatten([1, 2, 3, 4])
print flatten([1, [2, 3], [], 4, [5, [6, [7 ,8 ]]]])
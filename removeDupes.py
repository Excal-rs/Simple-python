def rmdup_set(list1):
    return list(set(list1))
# This will also sort the list in numerical order if only numbers but randomly if there are characters

def rmdup_dict(list2):
    return list(dict.fromkeys(list2))
# This will keep the original order

mylist = [1, 3, 'c', 'a', 'b', 2, 2, 4, 2, 3, 1, 4, 5, 6, 9, 9]

print(rmdup_set(mylist))
print(rmdup_dict(mylist))

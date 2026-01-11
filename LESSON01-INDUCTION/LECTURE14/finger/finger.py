# FelixOrion
# 251210 LunchBreak


def keys_with_value(aDict, target):
    """
    aDict: a dictionary
    target: an integer or string
    Assume that keys and values in aDict are integers or strings.
    Returns a sorted list of the keys in aDict with the value target.
    If aDict does not contain the value target, returns an empty list.
    """
    # Your code here
    my_list = []
    for k in aDict:
        if aDict[k] == target:
            my_list.append(k)
    return my_list


# Examples:
aDict = {1: 2, 2: 4, 5: 2}
target = 2
print(keys_with_value(aDict, target))  # prints the list [1,5]


def all_positive(d):
    """
    d is a dictionary that maps int:list
    Suppose an element in d is a key k mapping to value v (a non-empty list).
    Returns the sorted list of all k whose v elements sums up to a
    positive value.
    """
    # Your code here
    my_list = []
    for k in d:
        if sum(d[k]) > 0:
            my_list.append(k)
    return sorted(my_list)


# Examples:
d = {5: [2, -4], 2: [1, 2, 3], 1: [2]}
print(all_positive(d))  # prints the list [1, 2]

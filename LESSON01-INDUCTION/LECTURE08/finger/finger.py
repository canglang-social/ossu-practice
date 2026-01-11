# FelixOrion
# 251129 SecondClass


def same_chars(s1, s2):
    """
    s1 and s2 are strings
    Returns boolean True is a character in s1 is also in s2, and vice
    versa. If a character only exists in one of s1 or s2, returns False.
    """
    # Your code here
    for c1 in s1:
        if c1 not in s2:
            return False
    for c2 in s2:
        if c2 not in s1:
            return False
    return True


# Examples:
print(same_chars("abc", "cab"))  # prints True
print(same_chars("abccc", "caaab"))  # prints True
print(same_chars("abcd", "cabaa"))  # prints False
print(same_chars("abcabc", "cabz"))  # prints False

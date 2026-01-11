# Finger exercise:  Write a function isIn that accepts two strings as arguments and returns True if either string occurs anywhere in the other, and False otherwise.
# Hint: you might want to use the built-in str operation in.


def isIn(str1, str2):
    """Assumes str1 and str2 str.
    Returns True if either string occurs anywhere in the other, and False otherwise."""
    if (str1 in str2) or (str2 in str1):
        return True
    else:
        return False


def testIsIn():
    str1 = "apple"
    str2 = "pp"
    str3 = "st"
    resultTrue = isIn(str1, str2)
    resultTrueReverse = isIn(str2, str1)
    resultFalse = isIn(str3, str1)

    if resultTrue and resultTrueReverse:
        print("True Test Ok")

    if not resultFalse:
        print("False Test Ok")


testIsIn()

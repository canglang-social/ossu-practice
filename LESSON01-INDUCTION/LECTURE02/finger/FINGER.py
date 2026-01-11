# Finger Exercise Lecture 2
# Name: Felix Orion
# Collaborators: None
# Time Spent: 5m


def printNum(num):
    """
    num is numerical value
    """
    if num > 0:
        print("positive")
    elif num < 0:
        print("negative")
    else:
        print("zero")


num = int(input("input a number:"))
print(type(num))

if isinstance(num, (int, float, complex)):
    print("x is a number")
    printNum(num)
else:
    print("x is not a num")

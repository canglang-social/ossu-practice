# 251129 First Class
# Felix Orion

# Problem 1 - Bisection Search Practise
# Write a program using bisection search to find the forth root of a number inputted by the
# user. Print the forth root calculated with max error of 0.01.

x = float(input("Using bisection search calculate the forth root of: "))
epsilon = 0.01
if x < 0:
    print("error")
if x < 1:
    low = x
    high = 1
else:
    low = 0
    high = x
ans = (low + high) / 2
# first think x >=1
if x >= 1:
    while abs(ans**4 - x) >= epsilon:
        if ans**4 > x:
            high = ans
        else:
            low = ans
        ans = (low + high) / 2
else:
    while abs(ans**4 - x) >= epsilon:
        if ans**4 > x:
            low = ans
        else:
            high = ans
        ans = (low + high) / 2
print(f"the forth root of {x} is: {ans} with max error of {epsilon}")


# Problem 2 - Functions
# Write a Python function to check whether a number falls in a given range.
def check_in_range(num, range):
    """Assume num is int,range is range
    Return True if num falls in the range,otherwise False"""
    return num in range


# Problem 3 - Functions
# Write a Python function to check whether a number is perfect or not.
# (In number theory, a perfect number is a positive integer that is equal
# to the sum of its proper positive divisors, excluding the number itself).
# method1: find square root of num as high, then find all divisor
# method2:
def check_perfect(num):
    """
    Assume num is int
    Return True if num is a perfect num, otherwise False"""
    my_sum = 0
    for n in range(1, num):
        if num % n == 0:
            my_sum += n
    return my_sum == num


# Problem 4 - Approximation Algorithm (see Lecture 5 slides for similar problem)
# Write an approximation algorithm to calculate the forth root of some
# number inputted by the user.
# Print the result and the number of iterations required to reach that result.
# The program should not accept negative numbers. Initial parameters epsilon
# (i.e. accuracy), initial guess, increment and num_guesses are defined below.

# example initial parameters
epsilon = 0.01
ans = 0.0
increment = 0.001
num_guesses = 0

num = int(input("Type a positive num: "))
if num < 0:
    print("Negative num!")
else:
    while abs(ans**4 - num) >= epsilon and ans**4 <= num:
        ans += increment
        num_guesses += 1

    if abs(num_guesses**4 - num) >= epsilon:
        print("not find!")
    else:
        print(f"ans: {ans} num of guess: {num_guesses}")

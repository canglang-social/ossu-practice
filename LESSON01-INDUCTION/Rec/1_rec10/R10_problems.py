# FelixOrion
# 251215 ForthClass

#############################################################################
# Problem 1:
# For each of the following expressions, what is the order of growth class
# that best describes it?
# a) 8n
# b) 3n**2 + 7n**3 + 4
# c) 5log(n) + 5n
# d) 3**n + n**2
# e) 20n + nlog(n)
# f) 5 + 60
# g) log(n) + 4n

# n
# n**3
# n
# 3**n
# n log(n)
# 1
# n

#############################################################################
# Problem 2:
# Rank the following functions by runtime complexity. Note some may have
# the same runtime complexity.

# f(n) = n**2 + 4n + 2 # 4
# g(n) = log(n**2) # 6
# h(n) = log2(n)  (i.e. read as log base 2 n) # 6
# j(n) = 3n**3 + 2 # 3
# l(n) = n! # 1
# k(n) = 2**n  # 2


#############################################################################
# Problem 3:
# What is the time complexity for the following programs?


def program1():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    my_list_even = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            my_list_even.append(i)
    return my_list


# 1


def program2():
    my_list = [1, 2, 3, 4, 5, 7]
    my_second_list = [1, 2, 3, 4, 5, 7]

    output_list1 = [i for i in my_list]

    output_list2 = []
    for i in my_list:
        for j in my_second_list:
            output_list2 += [i, j]

    return (output_list1, output_list2)


# 1


def program3(n):
    epsilon = 0.01
    low = 0
    high = n
    ans = (high + low) / 2

    while abs(ans**4 - n) >= epsilon:
        if ans**4 > n:
            high = ans
        else:
            low = ans
        ans = (high + low) / 2
    return ans


# log(n)

#############################################################################
# Problem 4:
# Describe two ways to construct an algorithm to find the maximum number is a list.
# One algorithm should have time complexity O(n), the other O(n**2). (Note the
# O(n**2) algorithm is highly inefficient and we'd never actually use it
# in practice).


# n
def max_1(L):
    max = 0
    for i in L:
        if i > max:
            max = i
    return max


# n**2
def max_2(L):
    for i in range(len(L)):
        for j in range(len(L[i:])):
            if L[i + j] > L[i]:
                L[i], L[i + j] = L[i + j], L[i]
    print(L)
    return L[0]


print(max_2([5, 9, 8, 3, 0, 8]))

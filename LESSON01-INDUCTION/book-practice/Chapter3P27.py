# p27 Finger exercise
# Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no such pair of integers exists, it should print a message to that effect
x = int(input("Enter an integer: "))
ifFound = False
root = 0
pwr = 1
while pwr < 5:
    while root**pwr <= abs(x):
        if x < 0 and pwr % 2 == 0:
            break  # negative numbers can’t be even powers
        if root**pwr == abs(x):
            if x < 0:
                root = -root
            print(root, pwr)
            ifFound = True
            break
        root += 1
    if ifFound:
        break
    pwr += 1
if not ifFound:
    print("No pair of integers (root, pwr) found for", x)

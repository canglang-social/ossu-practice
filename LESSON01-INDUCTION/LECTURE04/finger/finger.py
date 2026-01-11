# Felix Orion
# 251127 SecondClass 5m

N = int(input("Enter a positive integer: "))

# Enum
guess = 1
while guess**3 < N:
    guess += 1
if guess**3 == N:
    print(guess)
else:
    print(ValueError)

# Finger exercise:  Add some code to the implementation of Newton-Raphson that keeps track of the number of iterations used to find the root. Use that code as part of a program that compares the efficiency of Newton-Raphson and bisection search. (You should discover that Newton-Raphson is more efficient.)

epsilon = 0.01
k = 25.0

# Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0
guess = k / 2.0
numGuess = 0
while abs(guess * guess - k) >= epsilon:
    print("guess", guess)
    guess = guess - (((guess**2) - k) / (2 * guess))
    numGuess += 1
print("Square root of", k, "is about", guess)
print("numGuess = ", numGuess)
print("----------------")

# bisection search
numGuesses = 0
low = 0.0
high = max(1.0, k)
ans = (high + low) / 2.0
while abs(ans**2 - k) >= epsilon:
    print("low =", low, "high =", high, "ans =", ans)
    numGuesses += 1
    if ans**2 < k:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print(ans, "is close to square root of", k)
print("numGuesses =", numGuesses)

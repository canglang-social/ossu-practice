# p34
# Finger exercise:  What would the code in Figure 3.4 do if the statement x = 25 were replaced by x = -25?
x = -25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low) / 2.0
while abs(ans**2 - x) >= epsilon:
    if numGuesses < 50:
        print("low =", low, "high =", high, "ans =", ans)
        numGuesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
print("numGuesses =", numGuesses)
print(ans, "is close to square root of", x)

# numGuesses will between 0 and 1. And program will never terminate.

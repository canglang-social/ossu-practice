# Felix Orion
# 251128 SelfReview

N = int(input("Type a num between 0 and 1000: "))

count = 0
low = 0
high = 1000

guess = (low + high) // 2
while guess != N:
    count += 1
    if guess > N:
        high = guess
    else:
        low = guess
    guess = (low + high) // 2
    print(guess, low, high)

print(f"count: {count}\nanswer: {guess}")

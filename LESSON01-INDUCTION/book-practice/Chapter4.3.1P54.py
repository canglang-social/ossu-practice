# Finger exercise: When the implementation of fib in Figure 4.7 is used to compute fib(5), how many times does it compute the value of fib(2) on the way to computing fib(5)?
# ans 3

global ans
ans = 0


def fib(n):
    """Assumes  int >=0
    Returns Fibonacci  n"""
    global ans
    if n == 2:
        ans += 1
        print("times of compute fib(2) in compute fib(5):", ans)
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def testFib(n):
    for i in range(n + 1):
        print("fib of ", i, "=", fib(i))


fib(5)

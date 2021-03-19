import sys


def factorial(n):
    if n <= 1:
        # Base Case
        return 1
    else:
        # Recursion Case
        return n * factorial(n-1)

# factorial(1000) # Recursion Max depth Error


sys.setrecursionlimit(1002)
print(sys.getrecursionlimit())
print(factorial(1000))

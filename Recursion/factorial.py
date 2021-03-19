from trace_recursion import trace


def factorial(n):
    if n <= 1:
        # Base Case
        return 1
    else:
        # Recursion Case
        return n * factorial(n-1)


# print(factorial(3))

assert factorial(4) == 24
assert factorial(5) == 120
assert factorial(-7) == 1
assert factorial(0) == 1
# assert factorial(1000) # Recursion Max depth Error

factorial = trace(factorial)
factorial(5)

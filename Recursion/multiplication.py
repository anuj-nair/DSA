from trace_recursion import trace


def mul(n, y):
    if n <= 0:
        return 0
    return y + mul(n-1, y)


mul = trace(mul)
print(mul(5, -4))
print(mul(7, 3))
print(mul(2, 100))

from trace_recursion import trace


def pow(n, y):
    if n <= 0:
        return 1
    return y * pow(n-1, y)


pow = trace(pow)
print(pow(5, 4))
print(pow(7, 3))
print(pow(2, 3))

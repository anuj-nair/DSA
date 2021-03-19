from trace_recursion import trace


def fibonacci_iter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fibonacci_recu(n):
    if n < 2:
        return n
    return fibonacci_recu(n - 1) + fibonacci_recu(n-2)


print(fibonacci_recu(10))

print(fibonacci_iter(10))

fibonacci_recu = trace(fibonacci_recu)
fibonacci_recu(5)

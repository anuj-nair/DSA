from trace_recursion import trace


def GCD(x, y):
    if y == 0:
        # Base Case
        return x
    else:
        # Recursive Case
        return GCD(y, x % y)


GCD = trace(GCD)
print(GCD(72, 96))
print(GCD(3, 6))
print(GCD(73, 37))

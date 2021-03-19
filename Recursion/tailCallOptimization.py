import inspect


def factorial(n):
    print("Non tail optimized stack size:", len(inspect.stack(0)))
    if n <= 1:
        # Base Case
        return 1
    else:
        # Recursion Case
        return n * factorial(n-1)


def attemptToTailCallOptimizedFactorial(n, accumulator=1):
    print("Attempted tail optimized stack size: ", len(inspect.stack(0)))
    if n == 0:
        return accumulator
    else:
        return tailCallOptimizedFactorial(n-1, accumulator=accumulator * n)


# print(factorial(5))
print(tailCallOptimizedFactorial(5))

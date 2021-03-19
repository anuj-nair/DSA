from trace_recursion import trace


def list_sum_iter(lt):
    s = 0
    for num in lt:
        s += num
    return s


def list_sum_recu(lt):
    if not len(lt):
        return 0
    return lt[0] + list_sum_recu(lt[1:])


# print("Iteration")
#print(list_sum_iter([3, 2, 1]))
# print("Recursion")
#print(list_sum_recu([3, 2, 1]))

assert list_sum_recu([1, 2, 4, 5]) == 12
assert list_sum_recu([3]) == 3
assert list_sum_recu([0, 10, -10, 12, -5, -1, -6]) == 0
assert list_sum_recu([14, -14, 14]) == 14
# assert factorial(1000) # Recursion Max depth Error

list_sum_recu = trace(list_sum_recu)
print(list_sum_recu([1, 2, 4, 5]))

from trace_recursion import trace


def qucikSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return qucikSort(left) + middle + qucikSort(right)


qucikSort = trace(qucikSort)
print(qucikSort([1, 4, 6, 66, 76, 66, 5, 5, 5, 5, 90, 1]))

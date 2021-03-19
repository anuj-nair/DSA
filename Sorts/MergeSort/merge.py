def merge(array, low, mid, high):
    i = low
    j = mid
    n = []
    while(i < mid and j < high):
        if(array[i] < array[j]):
            n.append(array[i])
            i = i+1
        else:
            n.append(array[j])
            j = j+1
    while(i < mid):
        n.append(array[i])
        i = i+1
    while(j < high):
        n.append(array[j])
        j = j+1
#    print('n', n)
    return n


def split(array, low, high):
    mid = int((high+low)/2)
#    print(low, mid, high)

    if mid > low:
        split(array=array, low=low, high=mid)
        split(array=array, low=mid, high=high)
    array[low:high] = merge(array=array, low=low, mid=mid, high=high)
#    print("array", array)
    return array


arr = [45, 2, 6, 4, 52, 2, 1, 6, 76, 35, 1, 45, 13, 1, 46, 33, 31, 13, 51, ]

print(split(array=arr, low=0, high=len(arr)))

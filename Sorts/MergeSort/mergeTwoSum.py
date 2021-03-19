result = None

chksum(a, tar, l, m, h):
    i = l, j = m, n = []
    c = 0
    while(i < m and j < h):
        if(a[i] >= tar):
            i++
            continue
        if(a[j] >= tar):
            j++
            continue
        if b == 0:
            if(a[i]+a[j] == tar):
                return = [i, j]
            else:
                if i == m-1:
                    i = l+1
                    j = m
                else:
                    j = j+1


divd(a, tar, l, h):
    if(l < h):
        m = int((l+h)/2)
        dvid(a, l, m)
        dvid(a, m+1, h)
        chk = chksum(a, tar, l, m, h)
        if chk is not None:
            global result = chk


nums = [3, 2, 4]

target = 6

ts = divd(nums, target, 0, len(nums))
print(result)

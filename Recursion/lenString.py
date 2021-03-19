from trace_recursion import trace


def str_len(n):
    if not n:
        return 0
    return 1 + str_len(n[1:])


str_len = trace(str_len)
print(str_len("Thomas"))
print(str_len("Ramu"))
print(str_len("ShivaRamaKrishnaIyer"))

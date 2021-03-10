import math


def mendelslaw(k, m, n):
    nk = math.comb(k + m + n, 2) - math.comb(m + n, 2)
    ms = math.comb(m, 2)
    nm = math.comb(m + n, 2) - math.comb(m, 2) - math.comb(n, 2)
    return (nk + ms * 0.75 + nm * 0.5) / math.comb(k + m + n, 2)


print(mendelslaw(21, 25, 24))

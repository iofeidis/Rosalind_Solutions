def rabbits(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return rabbits(n - 1, k) + k * rabbits(n - 2, k)


print(rabbits(32, 4))

def fibonnaci(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n - 1, k) + k * fibonnaci(n - 2, k)


print(fibonnaci(32, 4))

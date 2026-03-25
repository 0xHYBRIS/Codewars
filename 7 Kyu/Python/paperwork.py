def paperwork(n, m):
    if n * m <= 0 or (n < 0 and m < 0):
        return 0
    else:
        return n * m

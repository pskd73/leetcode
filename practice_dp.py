def is_it(l, n, s):
    if s == 0:
        return True
    if s > 0 and n == 0:
        return False
    return is_it(l, n-1, s) or is_it(l, n-1, s-l[n-1])


print(is_it([3, 34, 4, 12, 5, 2], 6, 9))
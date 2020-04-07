def minIncrementForUnique(A: list) -> int:
    if len(A) == 0 or len(A) == 1:
        return 0

    m = {}
    ans = 0
    
    unqs = []
    dups = []
    
    for i, n in enumerate(A):
        if n not in m:
            m[n] = True
        else:
            dups.append(n)

    unqs = list(m.keys())
    unqs.sort()
    dups.sort()
    
    ans = 0
    dups_head = 0
    unq_head = 1
    current_unq = unqs[1] if len(unqs) > 1 else None
    prev_unq = unqs[0]

    for n in dups:
        unqs.append(None)

    while dups_head < len(dups):
        print(current_unq, prev_unq, dups[dups_head])
        while current_unq == prev_unq + 1 or dups[dups_head] > prev_unq:
            unq_head += 1
            prev_unq = current_unq
            current_unq = unqs[unq_head]
        val = prev_unq + 1
        inc = val - dups[dups_head]
        print(dups[dups_head], inc)
        ans += inc
        prev_unq = val
        dups_head += 1
    return ans


# print(minIncrementForUnique([]))
# print(minIncrementForUnique([0,2,2]))
# print(minIncrementForUnique([0,0]))
# print(minIncrementForUnique([1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6]))
# print(minIncrementForUnique([3,2,1,2,1,7]))
# print(minIncrementForUnique([1, 2, 2]))
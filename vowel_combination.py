def get_next_state(state):
    next_starts_with = [sum(state), 0, 0, 0, 0]
    for i in range(1, 5):
        next_starts_with[i] = sum(state[i:])
    return next_starts_with

def get_combinations(n: int) -> int:
    if n == 1:
        return 5
    state = [5, 4, 3, 2, 1]
    for i in range(1, n-1):
        state = get_next_state(state)
    return sum(state)


print(get_combinations(5))
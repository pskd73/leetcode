def get_next_state(state):
    next_starts_with = [state[0], 0, 0, 0, 0]
    starts_with = state[1]
    for i in range(1, 5):
        next_starts_with[i] = sum(starts_with[i:])
    return (sum(next_starts_with), next_starts_with)

def get_combinations(n: int) -> int:
    if n == 1:
        return 5
    state = (15, [5, 4, 3, 2, 1])
    for i in range(1, n):
        state = get_next_state(state)
    return state[0]


print(get_combinations(5))
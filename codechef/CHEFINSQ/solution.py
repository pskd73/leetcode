def get_combinations(n, k):
    if k == 1:
        return n
    state = [x for x in range(n-1)]
    for tmp_k in range(1, k):
        tmp_state = state
        state = []
        for i in tmp_state:
            if i != n-1:
                for j in range(i+1, n):
                    state.append(j)
    return len(state)


def get_combinations_mat(n, k):
    cols = n
    rows = k
    mat = [[0 for y in range(cols)] for x in range(rows)]
    for i in range(cols):
        mat[0][i] = 1
    for row in range(1, rows):
        for col in range(1, cols):
            mat[row][col] = mat[row-1][col-1]+mat[row][col-1]
    return sum(mat[-1])


def get_ans(n, k, nums):
    sorted_nums = sorted(nums)
    sm = sum(sorted_nums[0:k])
    max_in_sum = max(sorted_nums[0:k])
    n_max_in_sum = len([x for x in sorted_nums[0:k] if x == max_in_sum])
    n_max_in_nums = len([x for x in nums if x == max_in_sum])
    return get_combinations_mat(n_max_in_nums, n_max_in_sum)

for t in range(int(input())):
    n, k = [int(x) for x in input().split(' ')]
    nums = [int(x) for x in input().split(' ')][:n]
    print(get_ans(n, k, nums))

# print(get_combinations_mat(9, 1))

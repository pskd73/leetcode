from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = []
        for row in range(len(matrix)):
            r = []
            for col in range(len(matrix[0])):
                r.append([0, 0, 0])
            dp.append(r)
        ans = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '1':
                    top = dp[row-1][col] if row-1 >= 0 else [0,0,0]
                    left = dp[row][col-1] if col-1 >= 0 else [0,0,0]
                    top_left = dp[row-1][col-1] if row-1 >= 0 and col-1 >= 0 else [0,0,0]

                    dp[row][col][0] = left[0]+1
                    dp[row][col][1] = top[1]+1
                    dp[row][col][2] = min(left[0], top[1], top_left[2])+1
                    ans = max(ans, dp[row][col][2])
        return ans**2


s = Solution()
p1 = [
    ['1','0','1','0','0'],
    ['1','0','1','1','1'],
    ['1','1','1','1','1'],
    ['1','0','0','1','0']
]
p2 = [["1"]]
p3 = [
    ["0","0","0","1"],
    ["1","1","0","1"],
    ["1","1","1","1"],
    ["0","1","1","1"],
    ["0","1","1","1"]
]
print(s.maximalSquare(p2))
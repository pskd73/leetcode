import sys

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:
                    continue
                top = sys.maxsize if row == 0 else grid[row-1][col]
                left = sys.maxsize if col == 0 else grid[row][col-1]
                grid[row][col] += min(top, left)
        return grid[-1][-1]

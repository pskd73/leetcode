class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[0 for c in range(n)] for r in range(m)]
        
        mat[0][0] = 1
        
        for row in range(m):
            for col in range(n):
                left, top = 0, 0
                if col > 0:
                    left = mat[row][col-1]
                if row > 0:
                    top = mat[row-1][col]
                mat[row][col] += left + top
                
        return mat[m-1][n-1]
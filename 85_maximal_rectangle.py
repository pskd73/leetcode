class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        x = len(matrix)
        if x == 0: return 0
        y = len(matrix[0])
        widths = [[0 for _ in range(y)] for _ in range(x)]
        max_area = 0
        for i in range(x):
            for j in range(y):
                if matrix[i][j] == '1':
                    if j == 0:
                        widths[i][j] = 1
                    else:
                        widths[i][j] = widths[i][j - 1] + 1
                    
                    w = widths[i][j]
                    for k in range(i, -1, -1):
                        if widths[k][j] == 0:
                            break
                        w = min(w, widths[k][j])
                        max_area = max(max_area, w * (i - k + 1))
                    
        return max_area

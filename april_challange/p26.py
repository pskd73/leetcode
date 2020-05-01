from collections import defaultdict

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mat = [[0 for x in text2] for y in text1]
        ans = 0
        for row in range(len(text1)):
            for col in range(len(text2)):
                top = mat[row-1][col] if row-1 >= 0 else 0
                left = mat[row][col-1] if col-1 >= 0 else 0
                top_left = mat[row-1][col-1] if row-1 >= 0 and col-1 >= 0 else 0
                if text1[row] == text2[col]:
                    mat[row][col] = top_left+1
                else:
                    mat[row][col] = max(top, left)
                ans = max(ans, mat[row][col])
        return ans
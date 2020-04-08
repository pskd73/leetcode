from typing import List

class Solution:
    def rotateBorder(self, matrix, row, col, n):
        end_index = n - 1
        nr, nc = row, col
        for i in range(end_index):
            carry = matrix[row][col+i]
            for j in range(4):
                if j == 0:
                    nr = row + i
                    nc = col + end_index
                elif j == 1:
                    nr = row + end_index
                    nc = col + end_index - i
                elif j == 2:
                    nr = row + end_index - i
                    nc = col
                elif j == 3:
                    nr = row
                    nc = col + i
                tmp = matrix[nr][nc]
                matrix[nr][nc] = carry
                carry = tmp



    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix) - 1):
            self.rotateBorder(matrix, i, i, len(matrix) - (i*2))


p1 = [
  [1,2,3,10],
  [4,5,6,11],
  [7,8,9,13],
  [14,15,16,17]
]

p2 = [
    [1,2],
    [3,4]
]
s = Solution()
s.rotate(p1)
print(p1)

[
    [14, 7, 4, 1], 
    [15, 8, 5, 2], 
    [16, 9, 6, 3], 
    [17, 13, 11, 10]
]
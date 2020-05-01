# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
    def __init__(self, mat):
        self.mat = mat
        self.counter = 0

    def get(self, x: int, y: int) -> int:
        self.counter += 1
        return mat[x][y]

    def dimensions(self) -> list:
        return len(self.mat), len(self.mat[0])


import sys


class Solution:
    def binSearch(self, binaryMat, row, m):
        frm, to = 0, m-1
        while frm < to:
            if frm+1 == to:
                if binaryMat.get(row, frm) == 1:
                    return frm
                if binaryMat.get(row, to) == 1:
                    return to
                return -1
            mid = frm + (to - frm)//2
            if binaryMat.get(row, mid) == 1:
                to = mid
            else:
                frm = mid
        return -1

    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        idxs = []
        for i in range(n):
            idx = self.binSearch(binaryMatrix, i, m)
            idxs.append(sys.maxsize if idx == -1 else idx)
        minIdx = min(idxs)
        return -1 if minIdx == sys.maxsize else minIdx



mat = [[0 for x in range(100)] for y in range(100)]
# mat = [
#     [0,0],
#     [1,1]
# ]

bm = BinaryMatrix(mat)
s = Solution()
print(s.leftMostColumnWithOne(bm))
print(bm.counter)

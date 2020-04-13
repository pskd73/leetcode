from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sums = {0: 0}
        s, ans = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                s -= 1
            else:
                s += 1
            if sums.get(s) is None:
                sums[s] = i+1
            else:
                ans = max(ans, i+1-sums[s])
        return ans

"""
0   1   2   3
1   1   0   0
1   2   1   0


 0   0   1   0   0   0   1   1   1   0   1   0   0   0   0   1   1   0
-1  -2  -1  -2  -3  -4  -3  -2  -1  -2  -1  -2  -3  -4  -5  -4  -3  -4

0   1   0   1
-1  0   -1  0
"""

s = Solution()
print(s.findMaxLength([0,1,0,1,0,0,0,0,0]))
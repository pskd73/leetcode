from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        grand_max, local_max = -999999, 0
        for n in nums:
            local_max += n
            grand_max = max(grand_max, local_max)
            local_max = max(local_max, 0)
        return grand_max



##
s = Solution()
# print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) #6
print(s.maxSubArray([-2,-1])) #-1
# print(s.maxSubArray([1, 2])) #3
# print(s.maxSubArray([8,-19,5,-4,20])) #21
# print(s.maxSubArray([0,-2,0])) #0
# print(s.maxSubArray([3,-2,2,0,-2,0])) #3
# print(s.maxSubArray([-1,0,-1,2,-3,1,2,3,-2])) #6
# print(s.maxSubArray([2,0,3,-2])) #5
# print(s.maxSubArray([0,-3,1,1])) #5
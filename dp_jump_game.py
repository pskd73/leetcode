from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        rt = 0
        
        for i in range(len(nums)):
            if i > rt:
                continue
            rt = max(rt, i+nums[i])
        return len(nums)-1 <= rt
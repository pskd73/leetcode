class Solution:
    def canJump(self, nums: List[int]) -> bool:
        rt = 0
        for i in range(len(nums)):
            if i > rt:
                return False
            rt = max(rt, i+nums[i])
        return len(nums)-1 <= rt

from typing import List

class Solution:
    def shift(self, nums, start, end, x):
        while start < end:
            if start+x > end:
                break
            tmp = nums[start]
            nums[start] = nums[start+x]
            nums[start+x] = tmp
            start += 1

    def moveZeroes(self, nums: List[int]) -> None:
        zeros = 0
        p1, p2 = 0, 0
        while p2 < len(nums):
            if nums[p2] == 0:
                self.shift(nums, p1, p2, zeros)
                p1 = p2-zeros
                zeros += 1
                p2 += 1
            else:
                if zeros == 0:
                    p1 += 1
                    p2 += 1
                else:
                    p2 += 1
        self.shift(nums, p1, min(p2, len(nums)-1), zeros)
##
p = [0,1,2,3,5,0,6,7,8,0,9]
s = Solution()
s.moveZeroes(p)
print(p)
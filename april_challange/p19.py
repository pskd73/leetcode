from typing import List

class Solution:
    def modInd(self, i, lst):
        return i%len(lst)

    def binary(self, nums, pivot, at_end, is_next):
        if len(nums) == 1:
            return at_end(0, 0)
        frm, to = pivot, pivot + len(nums)-1
        while frm < to:
            if frm+1 == to:
                return at_end(frm, to)
            mid = frm + ((to-frm)//2)
            if is_next(frm, to, mid):
                frm = mid
            else:
                to = mid
        return -1

    def search(self, nums: List[int], target: int) -> int:
        pivot = self.binary(
            nums, 
            0, 
            lambda frm, to: to if nums[frm] > nums[to] else frm, 
            lambda frm, to, mid: nums[self.modInd(mid, nums)] > nums[self.modInd(to, nums)]
        )

        def idxFromTo(frm, to):
            if nums[self.modInd(frm, nums)] == target:
                return frm
            elif nums[self.modInd(to, nums)] == target:
                return to
            return -1
            
        idx = self.binary(
            nums, 
            pivot, 
            idxFromTo, 
            lambda frm, to, mid: nums[self.modInd(mid, nums)] < target
        )
        if idx == -1:
            return -1
        return self.modInd(idx, nums)


s = Solution()
print(s.search([1], 8))
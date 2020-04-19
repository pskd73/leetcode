from typing import List

class Solution:
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
        def modInd(i):
            return i%len(nums)

        pivot = self.binary(
            nums, 
            0, 
            lambda frm, to: to if nums[frm] > nums[to] else frm, 
            lambda frm, to, mid: nums[modInd(mid)] > nums[modInd(to)]
        )

        def idxFromTo(frm, to):
            if nums[modInd(frm)] == target:
                return frm
            elif nums[modInd(to)] == target:
                return to
            return -1

        idx = self.binary(
            nums, 
            pivot, 
            idxFromTo, 
            lambda frm, to, mid: nums[modInd(mid)] < target
        )
        if idx == -1:
            return -1
        return modInd(idx)


s = Solution()
print(s.search([1], 8))
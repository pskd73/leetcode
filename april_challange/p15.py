from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = [1], [1]
        lp, rp = 1, 1
        for i in range(1, n):
            lp = lp*nums[i-1]
            rp = rp*nums[n-i]
            l.append(lp)
            r.append(rp)
        r = list(reversed(r))
        for i in range(n):
            l[i] = l[i]*r[i]
        return l


s = Solution()
print(s.productExceptSelf([1,2,3,4]))
from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(list)
        prv = 0
        ans = 0
        for i in range(len(nums)):
            tmp = prv + nums[i]
            sums[tmp].append(i)
            prv = tmp
        ksum = 0
        for i in range(len(nums)):
            x = (k-nums[i])+nums[i]+ksum
            if x in sums:
                for j in sums[x]:
                    if j >= i:
                        ans += 1
            ksum += nums[i]
        return ans


s = Solution()
print(s.subarraySum([0,0,0,0,0,0,0,0,0,0], 0))
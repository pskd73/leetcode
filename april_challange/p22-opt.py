from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sm, ans = 0, 0
        sums = defaultdict(int)
        sums[0] = 1
        for n in nums:
            sm += n
            ans += sums[sm-k]
            sums[sm] += 1
        return ans


s = Solution()
print(s.subarraySum([-1,-1,1], 0))
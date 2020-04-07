from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set()
        for n in arr:
            s.add(n)
        ans = 0
        for n in arr:
            if n+1 in s:
                ans += 1
        return ans

##
s = Solution()
print(s.countElements([1,2,3]))
print(s.countElements([1,1,3,3,5,5,7,7]))
print(s.countElements([1,3,2,3,5,0]))
print(s.countElements([1,1,2,2]))
from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        rotation = 0
        for r in shift:
            if r[0] == 1:
                rotation -= r[1]
            else:
                rotation += r[1]
        
        rotation = rotation % len(s)
        ans = ''
        for i in range(rotation, len(s)+rotation):
            ans += s[i%len(s)]
        return ans
        

s = Solution()
print(s.stringShift('abcdefg', [[1,1],[1,1],[0,2],[1,3]]))
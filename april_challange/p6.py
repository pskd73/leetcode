from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for i in range(len(strs)):
            mp[''.join(sorted(strs[i]))].append(strs[i])
        return list(mp.values())
            


##
s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
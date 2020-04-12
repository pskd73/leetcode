from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hl = [-x for x in stones]

        heapq.heapify(hl)

        while len(hl) > 1:
            y = -heapq.heappop(hl)
            x = -heapq.heappop(hl)
            if x != y:
                heapq.heappush(hl, x-y)

        return -hl[0] if len(hl) else 0


s = Solution()
print(s.lastStoneWeight([2,7,4,1,8,1]))
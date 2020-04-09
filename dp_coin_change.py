import sys
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [sys.maxsize for x in range(amount)]
        
        for n in coins:
            if n - 1 < len(dp):
                dp[n-1] = 1
            
        for i in range(len(dp)):
            amnt = i+1
            mins = [dp[i]]
            for c in coins:
                frm = amnt - c
                if frm > 0:
                    mins.append(dp[frm-1]+1)
            dp[i] = min(mins)
            
        return -1 if dp[-1] == sys.maxsize else dp[-1]
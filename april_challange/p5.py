from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        a, b = prices[0], prices[0]
        profit = 0
        for n in prices:
            if n > b:
                b = n
            else:
                profit += (b - a)
                a = n
                b = n
        if b > a:
            profit += (b - a)
        return profit


##
s = Solution()
print(s.maxProfit([7,1,5,3,6,4])) #7
print(s.maxProfit([1,2,3,4,5])) #4
print(s.maxProfit([7,6,4,3,1])) #0
print(s.maxProfit([])) #0
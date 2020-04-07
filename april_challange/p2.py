class Solution:
    def getNums(self, n: int):
        nums = []
        while n > 0:
            nums.append(n % 10)
            n = n // 10
        return nums
    
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            sum = 0
            for d in self.getNums(n):
                sum += d**2
            if sum in visited:
                return False
            n = sum
            visited.add(n)
        return True

##
s = Solution()
print(s.isHappy(1901))
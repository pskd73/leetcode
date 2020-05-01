from typing import List
from collections import defaultdict


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.count = defaultdict(int)
        self.first_uniq = []
        for n in nums:
            self.count[n] += 1
            if self.count[n]:
                self.first_uniq.append(n)
        self.curr_i = self.getNextUniq(0)

    def getNextUniq(self, i):
        for j in range(i, len(self.first_uniq)):
            if self.count[self.first_uniq[j]] == 1:
                return j
        return -1

    def showFirstUnique(self) -> int:
        return self.first_uniq[self.curr_i] if self.curr_i != -1 else -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        self.count[value] += 1
        if self.count[value] == 1:
            self.first_uniq.append(value)

        if self.curr_i == -1:
            self.curr_i = self.getNextUniq(len(self.first_uniq)-1)
        elif self.first_uniq[self.curr_i] == value:
            self.curr_i = self.getNextUniq(self.curr_i+1)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique([2,3,5])
# print(obj.showFirstUnique())
# obj.add(5)
# print(obj.showFirstUnique())
# obj.add(2)
# print(obj.showFirstUnique())
# obj.add(3)
# print(obj.showFirstUnique())

obj = FirstUnique([7,7,7,7,7,7,7,7,7])
print(obj.showFirstUnique())
obj.add(7)
obj.add(3)
obj.add(3)
obj.add(7)
obj.add(17)
print(obj.showFirstUnique())

# obj = FirstUnique([809])
# print(obj.showFirstUnique())
# obj.add(809)
# print(obj.showFirstUnique())
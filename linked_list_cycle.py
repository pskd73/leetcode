# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast, i = head, head.next, 0
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
            i += 1
        print(i)


p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)
p6 = ListNode(6)

p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
# p5.next = p6

def printLL(h):
    while h is not None:
        print(h.val)
        h = h.next

s = Solution()
print(s.hasCycle(p1))
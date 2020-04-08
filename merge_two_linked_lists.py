# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        nl = None
        curr = None
        while l1 is not None or l2 is not None:
            if l1 is None:
                n = ListNode(l2.val)
                l2 = l2.next
            elif l2 is None:
                n = ListNode(l1.val)
                l1 = l1.next
            elif l1.val < l2.val:
                n = ListNode(l1.val)
                l1 = l1.next
            else:
                n = ListNode(l2.val)
                l2 = l2.next

            if nl is None:
                nl = n
                curr = nl
            else:
                curr.next = n
                curr = curr.next

        return nl     


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

def printLL(h):
    while h is not None:
        print(h.val)
        h = h.next

s = Solution()
printLL(s.mergeTwoLists(p1, p6))
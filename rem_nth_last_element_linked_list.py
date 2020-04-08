# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rev(self, head):
        h = head
        prev = None
        while h is not None:
            tmp = h.next
            h.next = prev
            prev = h
            h = tmp
        return prev
        
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        rev_h = self.rev(head)
        print(rev_h)
        
        if n == 1:
            return self.rev(rev_h.next)
            
        i = 1
        h = rev_h
        prev = rev_h
        while h is not None:
            if i == n:
                prev.next = h.next
                break
            prev = h
            h = h.next
            i += 1
        
        return self.rev(rev_h)


p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)

p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5

def printLL(h):
    while h is not None:
        print(h.val)
        h = h.next

s = Solution()
printLL(s.removeNthFromEnd(p1, 3))
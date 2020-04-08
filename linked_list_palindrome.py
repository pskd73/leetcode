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

    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, l = head, head, 0
        while fast is not None:
            if not fast.next:
                l += 1
                break
            slow = slow.next
            fast = fast.next.next
            l += 2
        
        center = slow
        if l % 2 == 1:
            center = center.next

        center = self.rev(center)

        l1, l2 = head, center
        while l2 is not None:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next

        return True


p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(2)
p5 = ListNode(1)
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
print(s.isPalindrome(p1))
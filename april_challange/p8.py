# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

nodes = []
for i in range(6):
    n = ListNode(i+1)
    nodes.append(n)
    if i > 0:
        nodes[i-1].next = n

# n = nodes[0]
# while n != None:
#     print(n.val)
#     n = n.next

s = Solution()
print(s.middleNode(nodes[0]).val)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List

class Solution:
    def isSeq(self, node, arr, i, hasSibling):
        if node is None:
            if hasSibling:
                return False
            if i == len(arr):
                return True
            return False
        if i == len(arr):
            return False
        if node.val != arr[i]:
            return False
        return self.isSeq(node.left, arr, i+1, node.right is not None) or self.isSeq(node.right, arr, i+1, node.left is not None)

    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return self.isSeq(root, arr, 0, False)


# n1 = TreeNode(0)
# n2 = TreeNode(1)
# n3 = TreeNode(0)
# n1.left = n2
# n1.right = n3
# n4 = TreeNode(0)
# n5 = TreeNode(1)
# n2.left = n4
# n2.right = n5
# n6 = TreeNode(0)
# n3.left = n6
# n7 = TreeNode(1)
# n4.right = n7
# n8 = TreeNode(0)
# n9 = TreeNode(0)
# n5.left = n8
# n5.right = n9
# s = Solution()
# print(s.isValidSequence(n1, [0]))

n1 = TreeNode(8)
n2 = TreeNode(3)
n1.left = n2
s = Solution()
print(s.isValidSequence(n1, [8, 3, 8]))
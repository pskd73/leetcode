# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import sys

class Solution:
    def maxPath(self, node: TreeNode):
        """
        return: (maxPath, maxToNode)
        """
        if node is None:
            return -sys.maxsize, -sys.maxsize
        left = self.maxPath(node.left)
        right = self.maxPath(node.right)
        maxToNode = max(max(left[1], right[1])+node.val, node.val)
        maxPath = max(left[0], right[0], left[1]+right[1]+node.val, node.val, maxToNode)
        
        return maxPath, maxToNode

    def maxPathSum(self, root: TreeNode) -> int:
        return self.maxPath(root)[0]


# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n1.left = n2
# n1.right = n3
# s = Solution()
# print(s.maxPathSum(n1))

# n10 = TreeNode(-10)
# p9 = TreeNode(9)
# p20 = TreeNode(20)
# p15 = TreeNode(15)
# p7 = TreeNode(7)
# n10.left = p9
# n10.right = p20
# p20.left = p15
# p20.right = p7
# s = Solution()
# print(s.maxPathSum(n10))

# n = TreeNode(-3)
# s = Solution()
# print(s.maxPathSum(n))

n1 = TreeNode(-6)
n2 = TreeNode(-6)
n3 = TreeNode(2)
n4 = TreeNode(-6)
n5 = TreeNode(2)
n6 = TreeNode(-3)
n7 = TreeNode(-6)
n8 = TreeNode(9)
n9 = TreeNode(6)
n2.left = n1
n3.left = n2
n3.right = n4
n5.left = n3
n6.right = n5
n6.left = n7
n8.right = n6
n8.left = n9
s = Solution()
print(s.maxPathSum(n8))
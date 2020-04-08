# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtreeMirror(self, node1: TreeNode, node2: TreeNode) -> bool:
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False

        return self.isSubtreeMirror(node1.left, node2.right) and self.isSubtreeMirror(node1.right, node2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isSubtreeMirror(root.left, root.right)
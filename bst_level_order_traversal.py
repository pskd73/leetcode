# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import defaultdict

class Solution:
    def addToLevel(self, node, level, d):
        if node is None:
            return
        d[level].append(node.val)
        self.addToLevel(node.left, level+1, d)
        self.addToLevel(node.right, level+1, d)
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        d = defaultdict(list)
        self.addToLevel(root, 0, d)
        return d.values()
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rec(self, n) -> (int, int):
        if n is None:
            return 0, 0
        left_max_depth, left_max_diameter = self.rec(n.left)
        right_max_depth, right_max_diameter = self.rec(n.right)
        return max(left_max_depth, right_max_depth)+1, max(left_max_diameter, right_max_diameter, left_max_depth+right_max_depth+1)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ldt, ldm = self.rec(root.left)
        rdt, rdm = self.rec(root.right)
        return max(ldt+rdt+1, ldm, rdm)-1

nodes = [TreeNode(x) for x in range(6)]

nodes[1].left = nodes[2]
nodes[1].right = nodes[3]
nodes[2].left = nodes[4]
nodes[4].left = nodes[5]

s = Solution()
print(s.diameterOfBinaryTree(nodes[1]))
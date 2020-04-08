# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBSTValidSubtree(self, node: TreeNode, parentMin, parentMax, parentVal, frm):
        if node is None:
            return True
        if parentMin is not None and node.val <= parentMin:
            return False
        if parentMax is not None and node.val >= parentMax:
            return False
        return self.isBSTValidSubtree(
                node.left, 
                parentMin if frm == 'left' else parentVal, 
                node.val, 
                node.val,
                'left'
            ) and self.isBSTValidSubtree(
                node.right, 
                node.val, 
                parentMax if frm == 'right' else parentVal, 
                node.val,
                'right'
            )

    def isValidBST(self, root: TreeNode) -> bool:
        return self.isBSTValidSubtree(root, None, None, None, None)


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)

n2.left = n1
n2.right = n3
n3.right = n4
n4.right = n6
n4.left = n5


s = Solution()
print(s.isValidBST(n2))
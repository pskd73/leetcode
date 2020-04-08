class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def heightOfSubtree(self, root: TreeNode, depthOfParent):
        if root is None:
            return depthOfParent
        return max(self.heightOfSubtree(root.left, depthOfParent+1), self.heightOfSubtree(root.right, depthOfParent+1))
        
    
    def maxDepth(self, root: TreeNode) -> int:
        return self.heightOfSubtree(root, 0)



n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5
n4.left = n6

s = Solution()
print(s.maxDepth(n1))
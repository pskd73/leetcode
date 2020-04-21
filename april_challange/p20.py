# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
from typing import List

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        stack = []
        root = TreeNode(preorder[0])
        stack.append([root, root.val, sys.maxsize, 'r'])
        stack.append([root, -sys.maxsize, root.val, 'l'])
        i = 1
        while len(stack) and i < len(preorder):
            top = stack.pop()
            cur = preorder[i]
            # print('cmp', cur, top[1], top[2])
            if cur > top[1] and cur < top[2]:
                # print('adding', cur)
                tmp = TreeNode(cur)
                stack.append([tmp, cur, top[2], 'r'])
                stack.append([tmp, top[1], cur, 'l'])
                if top[3] == 'l':
                    top[0].left = tmp
                else:
                    top[0].right = tmp
                i += 1
        return root



def printTree(node: TreeNode):
    if node is None:
        return
    print(node.val)
    printTree(node.left)
    printTree(node.right)


s = Solution()
printTree(s.bstFromPreorder([5,2,1,3,12,9,21,19,25]))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from treenode import TreeNode
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stk = []
        res = []
        while root:
            stk.append(root)
            root = root.left
        while stk:
            top = stk.pop()
            res.append(top.val)
            if top.right:
                cur = top.right
                while cur:
                    stk.append(cur)
                    cur = cur.left
        return res

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from treenode import TreeNode
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        def isSubtree(pRoot1, pRoot2):
            if not pRoot2:
                return True
            if not pRoot1:
                return False
            return pRoot1.val == pRoot2.val \
                   and isSubtree(pRoot1.left, pRoot2.left) \
                   and isSubtree(pRoot1.right, pRoot2.right)
        if not pRoot1 or not pRoot2:
            return False
        return isSubtree(pRoot1, pRoot2) \
               or self.HasSubtree(pRoot1.left, pRoot2) \
               or self.HasSubtree(pRoot1.right, pRoot2)
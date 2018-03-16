from treenode import TreeNode
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(nodeL, nodeR):
            if not nodeL or not nodeR:
                if not nodeL and not nodeR:
                    return True
                else:
                    return False
            return nodeL.val == nodeR.val \
                    and helper(nodeL.left, nodeR.right) and helper(nodeL.right, nodeR.left)

        if not root:
            return True
        return helper(root.left, root.right)
from treenode import TreeNode
class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        prev = TreeNode(-1) # fake node
        res = []
        if not root:
            return res
        stk = []
        stk.append(root)
        while stk:
            top = stk[-1]
            if top.left and top.left is not prev and top.right != prev:
                cur = top.left
                while cur:
                    stk.append(cur)
                    cur = cur.left
            elif top.right and top.right is not prev:
                cur = top.right
                while cur:
                    stk.append(cur)
                    cur = cur.left
            else:
                prev = stk.pop()
                res.append(prev.val)
        return res

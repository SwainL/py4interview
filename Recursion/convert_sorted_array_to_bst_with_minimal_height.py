from treenode import TreeNode
class Solution:
    """
    @param: A: an integer array
    @return: A tree node
    """
    def sortedArrayToBST(self, A):
        # write your code here
        def helper(start, end):
            if start > end:
                return None
            mid = start + (end - start) // 2
            root = TreeNode(A[mid])
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)
            return root
        return helper(0, len(A) - 1)

from listnode import ListNode
class Solution:
    """
    @param: node: the node in the list should be deletedt
    @return: nothing
    """
    def deleteNode(self, node):
        # write your code here
        node.val = node.next.val
        node.next = node.next.next
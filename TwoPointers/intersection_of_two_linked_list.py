# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodeA, nodeB = headA, headB
        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        return nodeA # only 2 ways to get out of the loop, they meet or the both hit the end=None


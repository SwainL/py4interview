# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        isCycle = False
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                isCycle = True
                break
        if not isCycle:
            return None

        # critical section
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
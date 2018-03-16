# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # move slow pointer to the middle of the linked list
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half of the list, and the prev is the new head
        prev, cur = None, slow
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # compare two list, namely head and prev
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
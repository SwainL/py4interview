from listnode import ListNode
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        left, cur = dummy, head
        k = n - m + 1
        while m > 1:
            left = cur
            cur = cur.next
            m -= 1
        # reserve k times
        start = cur
        prev = None
        while k:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            k -= 1
        # connect together
        left.next = prev
        start.next = cur
        return dummy.next
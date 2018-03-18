from listnode import ListNode, construct_list, print_list


class Solution:
    def swap_odd_nodes_with_even_nodes(self, head):
        # e.g 1->4->5->3->2->8
        #     4->1->3->5->8->2
        if not head:
            return None
        if not head.next:
            return head
        res = head.next
        node = head.next.next
        head.next.next = head
        head.next = self.swap_odd_nodes_with_even_nodes(node)
        return res

    def put_even_numbers_before_odd_numbers(self, head):
        dummy_even = ListNode(-1)
        cur = dummy_even
        dummy_odd = ListNode(-1)
        cur_odd = dummy_odd
        while head:
            if head.val % 2 == 0:
                cur.next = head
                cur = cur.next
            else:
                cur_odd.next = head
                cur_odd = cur_odd.next
            head = head.next
        # critical: cut ending
        cur.next, cur_odd.next = None, None
        cur.next = dummy_odd.next
        return dummy_even.next


head = construct_list([1, 4, 5, 3, 2, 8])
head = Solution().put_even_numbers_before_odd_numbers(head)
print_list(head)

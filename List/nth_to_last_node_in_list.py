from listnode import construct_list


class Solution:
    """
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: Nth to last node of a singly linked list.
    """

    def nthToLast(self, head, n):
        # write your code here
        if n <= 0:
            return None
        left = head
        right = head
        while n > 1:
            right = right.next
            if not right:
                return None
            n -= 1
        while right.next:
            right = right.next
            left = left.next
        return left


sol = Solution()
head = construct_list([1, 7, 3, 9, 5])
node = sol.nthToLast(head, 2)
print(node.val)

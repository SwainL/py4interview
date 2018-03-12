# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list(head):
    while head:
        print(head.val, end="->")
        head = head.next
    print("null")


def construct_list(arr):
    if not arr or len(arr) == 0:
        return None
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head

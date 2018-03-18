from collections import deque
class DLinkedNode:

    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.frequency = 1
        self.prev = None
        self.post = None

class DoubleEndCycleList:

    def __init__(self, head, tail):
        self.head = DLinkedNode(-1, -1) # dummy head
        self.tail = DLinkedNode(-1, -1) # dummy tail

        # connected to a circle
        self.head.prev = self.tail
        self.head.post = self.tail
        self.tail.prev = self.head
        self.tail.post = self.head

    def add2Head(self, node):
        # add node after the dummy head in O(1)
        original_true_head = self.head.post
        node.pre = self.head
        node.post = original_true_head

        self.head.post = node
        original_true_head.pre = node

    def removeNode(self, node):
        # remove node in O(1)
        node.pre.post = node.post
        node.post.pre = node.pre

    def popTail(self):
        node = self.tail.pre
        self.removeNode(node)
        return node

    def moveNode2Head(self, node):
        # move node to head in O(1)
        self.removeNode(node)
        self.add2Head(node)

    def isEmpty(self):
        if self.head.post is self.tail:
            return True
        return False


class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.tab = dict() # key -> node
        self.freqs = [None] * (capacity + 1) # frequency -> DoubleEndCycleList
        self.indicator = 1 # indicator for least frequency

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.tab:
            return -1
        node = self.tab[key]
        frequency = node.frequency
        self.freqs[frequency].moveNode2Head(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.tab:
            node = self.tab[key]
            node.val = value
            self.tab[node.frequency].moveNode2Head(node)
        else:
            if len(self.tab) >= self.capacity:
                



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class DLinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.post = None

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.tab = dict()
        self.head = DLinkedNode(-1, -1) # dummy head
        self.tail = DLinkedNode(-1, -1) # dummy tail
        self.head.post = self.tail
        self.tail.pre = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.tab:
            self.__moveNode2Head(self.tab[key])
            return self.tab[key].val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # Important! : to judge if it exist already
        if key in self.tab:
            self.tab[key].val = value
            self.__moveNode2Head(self.tab[key])
            return
        if len(self.tab) >= self.capacity:
            evict_node = self.__popTail()
            del self.tab[evict_node.key]
        node = DLinkedNode(key, value)
        self.__add2Head(node)
        self.tab[key] = node

    # Section in regard with DLinkedNode
    def __add2Head(self, node):
        # add node after the dummy head in O(1)
        original_true_head = self.head.post
        node.pre = self.head
        node.post = original_true_head

        self.head.post = node
        original_true_head.pre = node

    def __removeNode(self, node):
        # remove node in O(1)
        node.pre.post = node.post
        node.post.pre = node.pre

    def __popTail(self):
        node = self.tail.pre
        self.__removeNode(node)
        return node

    def __moveNode2Head(self, node):
        # move node to head in O(1)
        self.__removeNode(node)
        self.__add2Head(node)

    def __printDLinkedList(self):
        cur = self.head
        while cur:
            if cur.post:
                print(cur.key, end="->")
            else:
                print(cur.key)
            cur = cur.post


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
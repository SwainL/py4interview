# -*- coding:utf-8 -*-
from heapq import heappush, heapreplace
class Solution:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
    def Insert(self, num):
        # write code here
        if len(self.max_heap) <= len(self.min_heap):
            heappush(self.max_heap, -num)
            if len(self.min_heap) > 0 and -self.max_heap[0] > self.min_heap[0]:
                max_top = -self.max_heap[0]
                self.max_heap[0] = -self.min_heap[0]
                heapreplace(self.min_heap, max_top)
        else:
            heappush(self.min_heap, num)
            if self.min_heap[0] < -self.max_heap[0]:
                max_top = -self.max_heap[0]
                heapreplace(self.max_heap, -self.min_heap[0])
                self.min_heap[0] = max_top
    def GetMedian(self):
        # write code here
        return -self.max_heap[0]

sol = Solution()
sol.Insert(10)
print(sol.GetMedian())
sol.Insert(5)
print(sol.GetMedian())
sol.Insert(20)
print(sol.GetMedian())
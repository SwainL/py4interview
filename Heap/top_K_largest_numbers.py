from heapq import heappush, heapreplace, heappop
from collections import deque
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heappush(min_heap, num)
            else:
                if num > min_heap[0]:
                    heapreplace(min_heap, num)
        res = deque()
        while min_heap:
            res.appendleft(heappop(min_heap))
        return list(res)
print(Solution().topk([10, 5, 10], 2))
from heapq import heappush, heapreplace
class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        max_heap = []
        min_heap = []
        res = []
        for i in range(len(nums)):
            if i % 2 == 0:
                heappush(max_heap, -nums[i])
                if len(min_heap) > 0 and -max_heap[0] > min_heap[0]:
                    max_top = -max_heap[0]
                    max_heap[0] = -min_heap[0]
                    heapreplace(min_heap, max_top)
            else:
                heappush(min_heap, nums[i])
                if min_heap[0] < -max_heap[0]:
                    max_top = -max_heap[0]
                    heapreplace(max_heap, -min_heap[0])
                    min_heap[0] = max_top
            res.append(-max_heap[0])
        return res


sol = Solution()
nums = [4, 5, 1, 3, 2, 6, 0]
print(sol.medianII(nums))
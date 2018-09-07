class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        tmp = Counter(nums)
        s_tmp = sorted(tmp.items(), key=lambda item:item[1], reverse=True)
        return [num for num, _ in s_tmp[:k]]
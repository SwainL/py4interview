class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        firstSet = set()
        secndSet = set()
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[j] == nums[i]:
                    continue;


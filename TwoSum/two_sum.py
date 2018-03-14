class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        val_to_idx = dict()
        for i, num in enumerate(nums):
            if target - num in val_to_idx:
                return [val_to_idx[target - num], i]
            else:
                val_to_idx[num] = i
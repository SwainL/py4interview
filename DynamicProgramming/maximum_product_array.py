class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        minPrd, maxPrd = nums[0], nums[0]
        for num in nums[1:]:
            # Important Note: must assign prallelly
            maxPrd, minPrd = max(minPrd*num, maxPrd*num, num), min(minPrd*num, maxPrd*num, num)
            res = max(res, maxPrd)
        return res
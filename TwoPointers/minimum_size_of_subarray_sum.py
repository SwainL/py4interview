class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sums = [num for num in nums]
        for i in range(1, nums):
            sums[i] += sums[i - 1]
        if sums[-1] < s:
            return 0
        left, right = 0, 0
        res = len(nums)
        while left == 0 and left <= right:
            if nums[right] - nums[left] >= s:
                res = min(res, right - left + 1)
                left += 1
            else:
                right += 1
        return res

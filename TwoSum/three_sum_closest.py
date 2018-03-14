class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = nums[0] + nums[1] + nums[2]
        list.sort(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == target:
                    return target
                elif three_sum > target:
                    right -= 1
                else:
                    left += 1

                if abs(three_sum - target) < abs(res - target):
                    res = three_sum
        return res

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list.sort(nums)
        res = []
        for i, target in enumerate(nums):
            # remove repetition
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            # 2 sum
            left, right = i + 1, len(nums) - 1
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == -target:
                    res.append([nums[i], nums[left], nums[right]])
                    # remove repetition
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    while right > left and nums[right - 1] == nums[right]:
                        right -= 1
                    # find all two numbers sum of which is -target
                    left += 1
                    right -= 1
                elif two_sum > -target:
                    right -= 1
                else:
                    left += 1
        return res



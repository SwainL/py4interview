class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lastUniquePos = -1
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lastUniquePos += 1
            nums[lastUniquePos] = nums[i]
        return lastUniquePos + 1
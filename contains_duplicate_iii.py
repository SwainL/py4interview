class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 1 or t < 0:
            return False
        key_to_val = dict()
        for idx, val in enumerate(nums):
            key = val // (t + 1)
            for candidate in (key - 1, key, key + 1):
                if candidate in key_to_val and abs(key_to_val[candidate] - val) <= t:
                    return True
            if len(key_to_val) == k:
                del key_to_val[nums[idx - k] // (t + 1)]
            key_to_val[key] = val
        return False



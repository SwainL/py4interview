def quickSort(nums):
    # helper(0, len(nums) - 1)

    def helper(start, end):
        if start >= end:
            return
        idx = partition(start, end)
        helper(start, idx - 1)
        helper(idx + 1, end)

    def partition(lo, hi):
        if lo == hi:
            return lo
        start = lo
        pivot = nums[lo]
        lo += 1
        while lo <= hi:
            if nums[lo] >= pivot:
                nums[hi], nums[lo] = nums[lo], nums[hi]
                hi -= 1
            else:
                lo += 1
        nums[start], nums[hi] = nums[hi], pivot
        return hi

    helper(0, len(nums) - 1)

arr = [54,26,93,17,77,31,44,55,20, 4, 7, 2, 10, 5, 1, 89, 200]
# arr = [4, 7, 2, 10, 5, 1]
quickSort(arr)
print(arr)
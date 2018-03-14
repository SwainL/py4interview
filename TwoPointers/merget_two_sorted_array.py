class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, cur = m - 1, n - 1, m + n - 1
        while cur >= 0 and p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[cur] = nums1[p1]
                p1 -= 1
            else:
                nums1[cur] = nums2[p2]
                p2 -= 1
            cur -= 1
        while p2 >= 0:
            nums1[cur] = nums2[p2]
            p2 -= 1
            cur -= 1
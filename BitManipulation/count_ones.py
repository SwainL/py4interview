# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        # python only
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = n & (n - 1)
        return count

print(Solution().NumberOf1(-7))
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        # bubbling sort
        for i in range(len(array)):
            j = i
            while j > 0 and array[j] %2 != 0 and array[j - 1] % 2 == 0:
                array[j], array[j - 1] = array[j - 1], array[j]
                j -= 1


array = [1, 2, 3, 4, 5, 6]
Solution().reOrderArray(array)
print(array)
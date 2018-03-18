from collections import deque

# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        # maintain a non-increasing double-end list, like 5->5->4->2->2->1
        # important note: the elements in double-end list is index of the corresponding number, instead of number
        # add() operation:
        # step 1: while deque and num[new_idx] > num[deque[-1]]: deque.pop_from_right();
        # step 2: deque.push_from_bear(new_idx)
        # getMax() operation:
        # step 1: pop index which diff(cur_idx, index) > size from front
        # step 2: return num[deque[0]]
        que = deque()
        res = []
        if size <= 0:
            return res
        for idx, val in enumerate(num):
            # add()
            while que and val > num[que[-1]]:
                que.pop()
            que.append(idx)
            # getMax()
            while que and idx - que[0] >= size:
                que.popleft()
            res.append(num[que[0]])
        return res[size - 1:]

num = [2, 3, 4, 2, 6, 2, 5, 1]
size = 3
res = Solution().maxInWindows(num, size)
print(res)
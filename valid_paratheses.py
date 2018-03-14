class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {"}": "{", ")": "(", "]": "["}
        stack = list()
        for p in s:
            if p in mapping.values():
                stack.append(p)
            else:
                if not stack or stack.pop() != mapping[p]:
                    return False
        return len(stack) == 0

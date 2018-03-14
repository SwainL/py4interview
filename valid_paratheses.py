class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        for p in s:
            if p in ("{", "(", "["):
                stack.append(p)
            else:
                if not stack or stack.pop() != p:
                    return False
        return True

print(Solution().isValid("[]([])"))
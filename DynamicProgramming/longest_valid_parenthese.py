class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0] * len(s)
        for i in range(1, len(dp)):
            if s[i] == "(":
                dp[i] = 0
            else:
                if s[i - 1] == "(":
                    dp[i] = 2 + dp[i - 2]
                else:
                    pos = i - dp[i - 1] - 1
                    if pos < 0 or s[pos] != "(":
                        dp[i] = 0
                    else:
                        dp[i] = 2 + dp[i - 1]
                        if pos - 1 >= 0:
                            dp[i] += dp[pos - 1]
        return max(dp)

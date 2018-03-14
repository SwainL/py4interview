class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        num = a ^ b
        count = 0
        while num != 0:
            count += num & 1
            num = rshift(num, 1)
        return count
def rshift(val, n):
    return val>>n if val >= 0 else (val+0x100000000)>>n

sol = Solution()
print(sol.bitSwapRequired(1, -1))

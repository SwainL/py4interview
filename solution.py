def helper(nums, sum):
    m = len(nums)
    n = sum + 1
    dp = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        if nums[i] in range(n):
            dp[i][nums[i]] = 1
    print(dp[0])
    for i in range(1, m):
        for j in range(n):
            dp[i][j] += dp[i - 1][j]
            if j - nums[i] in range(n):
                dp[i][j] += dp[i - 1][j - nums[i]]
        print(dp[i])
    return dp[m - 1][n - 1]

nums = [4, 3, 2, 3, 5, 2, 1]

print(helper(nums, 5))
'''
DP Skeleton

# nums = input list
dp = [0]*(len(nums)+1)  # or True/False depending on problem
dp[0] = base_case

for i in range(1, len(nums)+1):
    dp[i] = transition(dp, i, nums)

return dp[-1]
'''

# 1D DP example: climbing stairs
def dp_1d(n):
    dp = [0] * (n + 1)
    dp[0] = 1  # 0 ways to climb 0 stairs
    dp[1] = 1  # 1 way to climb 1 stair
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # sum of last 2 steps
    return dp[n]

# 2D DP example: unique paths in a grid
def dp_2d(rows, cols):
    dp = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        dp[r][0] = 1  # only one way in first column
    for c in range(cols):
        dp[0][c] = 1  # only one way in first row
    for r in range(1, rows):
        for c in range(1, cols):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]  # sum of top + left
    return dp[rows - 1][cols - 1]

# Subset sum DP: for min difference / knapsack type problems
def subset_sum(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]
    return dp[target]

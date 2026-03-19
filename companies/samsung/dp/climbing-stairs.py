def climbingStairs(n):
    # dp[i] = number of ways to reach step i
    dp = [0] * (n + 1)
    
    # base cases: 1 way to reach step 0 and step 1
    dp[0] = 1
    dp[1] = 1
    
    # to reach step i, you came from step i-1 (1 step) or step i-2 (2 steps)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    # Time: O(n), Space: O(n)
    return dp[n]
def houseRobber(nums):
    # if no nums list, return 0. No houses can be robbed
    if not nums:
        return 0
    
    # let n be the length of the list, where dp is a list of 0s (default value) with a length of n + 1
    n = len(nums)
    dp = [0] * (n + 1)
    
    # set base cases, dp[0] to be the first number in nums and dp[1] to be the maximum value between nums[0] and nums[1]
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    # to reach step i, you need to get the max between step i - 1 and step i - 2 + nums[i] 
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    
    # return the maximum amount of money robable from all n houses
    # Time: O(n) and Space: O(n)
    return dp[n - 1]
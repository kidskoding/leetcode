def maximumSubarray(nums) -> int:
    # if there no nums list, return 0
    if not nums:
        return 0
    
    n = len(nums)
    dp = [0] * n
    
    # base case - first element is its own subarray
    dp[0] = nums[0]
    
    for i in range(2, n):
        # either start fresh at nums[i] or extend previous subarray
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
        
    # return the maximum subarray sum found
    # Time: O(n), Space: O(n)
    return max(dp[:n])
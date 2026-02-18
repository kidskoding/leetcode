def maximum_subarray_sum(nums):
    # 1. Let maxSum be a variable that stores the maximum sum found so far
    maxSum = nums[0]
    
    # 2. Let currMaxSum be the maximum sum at the subarray ending at the current position
    currMaxSum = nums[0]
    
    # Loop through nums
    for i in range(1, len(nums)):
        # 3. Decide whether to extend the current maximum sum or start a new maximum sum
        currMaxSum = max(nums[i], currMaxSum + nums[i])
        
        # 4. Update the global maximum sum so far
        maxSum = max(maxSum, currMaxSum)
    
    # 5. Return the maximum sum subarray
    return maxSum
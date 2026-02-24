def maxSubarraySum(nums):
    # 1. Let maxSoFar be the maximum overall sum of a subarray found so far
    maxSoFar = nums[0]
    
    # 2. Let currMaxSoFar be the maximum overall sum of a subarray found currently
    currMaxSoFar = nums[0]
    
    # Loop through nums
    for i in range(1, len(nums)):
        # 3. Update currMaxSoFar to be whichever one of the two is a greater value: 
        #       currMaxSoFar itself or currMaxSoFar + nums[i]
        #       This will determine whether to extend the current subarray sum found so far or 
        #       to start a new maximum sum subarray
        currMaxSoFar = max(nums[i], currMaxSoFar + nums[i])
        
        # 4. Update maxSoFar to be the maximum of the maximum sum found so far or the current maximum sum found so far
        maxSoFar = max(maxSoFar, currMaxSoFar)
    
    # 5. Return the maximum sum subarray found in nums
    return maxSoFar
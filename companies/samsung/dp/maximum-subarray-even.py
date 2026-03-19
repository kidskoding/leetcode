def maximumSubarrayEven(nums) -> int:
    if not nums:
        return 0
    
    n = len(nums)
    dp_even = [float('-inf')] * n
    dp_odd = [float('-inf')] * n
    
    # base case
    if nums[0] % 2 == 0:
        dp_even[0] = nums[0]
    else:
        dp_odd[0] = nums[0]
    
    for i in range(1, n):
        if nums[i] % 2 == 0:
            # even number
            if dp_even[i-1] != float('-inf'):
                dp_even[i] = dp_even[i-1] + nums[i]
            dp_even[i] = max(dp_even[i], nums[i])
            
            if dp_odd[i-1] != float('-inf'):
                dp_odd[i] = dp_odd[i-1] + nums[i]
        
        else:
            # odd number
            if dp_odd[i-1] != float('-inf'):
                dp_even[i] = dp_odd[i-1] + nums[i]
            
            if dp_even[i-1] != float('-inf'):
                dp_odd[i] = dp_even[i-1] + nums[i]
            dp_odd[i] = max(dp_odd[i], nums[i])
    
    return max(dp_even) if max(dp_even) != float('-inf') else 0
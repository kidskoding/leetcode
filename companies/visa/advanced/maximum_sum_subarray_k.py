def maxSumSubarraySizek(nums, k):
    # 1. Let window_sum be the sum of the first k elements
    window_sum = sum(nums[:k])
    
    # 2. Let max_sum be the maximum sum possible of a subarray of size k
    max_sum = window_sum
    
    # Slide the window by looping through the elements in nums from k to the end
    for i in range(k, len(nums)):
        # 3. Slide the window by subtracting window_sum from the first element in the window (nums[i - k])
        #   and adding it to the next element in nums (nums[i])
        window_sum = window_sum - nums[i - k] + nums[i]
        
        # 4. Update max_sum to be the maximum sum of max_sum and window_sum
        max_sum = max(max_sum, window_sum)
    
    # 5. Return max_sum
    return max_sum
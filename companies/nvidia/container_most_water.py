def containerMostWater(heights):
    # 1. Create two pointers left and right, which will represent two ends of the heights array
    left, right = 0, len(heights) - 1
    
    # 2. Create a variable that stores the max area throughout the max array
    maxArea = 0
    
    # 3. Traverse through the array
    while left < right:
        # 4. Calculate the current area and update the maxArea
        # The max water that can be held is the of heights[left] and heights[right]
        area = (right - left) * min(heights[left], heights[right])
        maxArea = max(area, maxArea)
        
        # 5. Update the left and right pointers! If heights[left] > heights[right], we know that we need to move
        # the right pointer back because we need to move the pointer that has the smaller value since we need the greatest area
        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
    
    # 6. Return the maxArea
    return maxArea
def maxArea(height):
    maxArea = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        area = (right - left) * min(height[left], height[right])
        maxArea = max(maxArea, area)
        
        if height[left] > height[right]:
            left += 1
        else:
            right -= 1
            
    return maxArea

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))
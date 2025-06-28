def sortColors(nums):
    left, right = 0, len(nums) - 1
    i = 0
    
    while i <= right:
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        else:
            i += 1
            
    return nums

print(sortColors([2,0,2,1,1,0]))
print(sortColors([2,0,1]))
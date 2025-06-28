def moveZeroes(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] == 0:
            del nums[left]
            nums.append(0)
            right -= 1
        elif nums[right] == 0:
            del nums[right]
            nums.append(0)
            left += 1
        else:
            left += 1
            right -= 1

    if nums[left] == 0:
        del nums[left]
        nums.append(0)

    return nums

## Other Solution
def moveZeroesBetter(nums):
    nextNonZero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[nextNonZero], nums[i] = nums[i], nums[nextNonZero]
            nextNonZero += 1

print(moveZeroes([0,1,0,3,12]))
print(moveZeroes([0]))
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n
    prefix = suffix = 1
    
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
        
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
        
    return res

print(productExceptSelf([1,2,4,6]))
print(productExceptSelf([-1,0,1,2,3]))
def twoSum(nums, target):
    dict = {}
    
    for (i, x) in enumerate(nums):
        if x in dict.keys():
            return [dict[x], i]
        else:
            complement = target - x
            dict[complement] = i
            
    return []

print(twoSum(nums = [3,4,5,6], target = 7))
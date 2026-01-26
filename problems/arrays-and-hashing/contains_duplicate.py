def containsDuplicate(nums):
    map = {}
    
    for x in nums:
        if x in map:
            return True

        map[x] = 0
        
    return False

print(containsDuplicate([1, 2, 3, 3]))
print(containsDuplicate([1, 2, 3, 4]))
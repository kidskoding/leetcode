from typing import List

def hasDuplicate(nums: List[int]) -> bool:
    nums_set = set(nums)
    return len(nums_set) != len(nums)

print(hasDuplicate([1, 2, 3, 3]))
print(hasDuplicate([1, 2, 3, 4]))
# TEMPLATES - ARRAYS AND HASHING

def arrays_and_hashing(nums):
    # Create a set to keep track of numbers we've seen so far
    seen = set()
    
    # Iterate through each number in the input array
    for x in nums:
        # If the number is already in the set, we've found a duplicate
        if x in seen:
            return True
        
        # Otherwise, add the number to the set and continue
        seen.add(x)
        
    # Return False if no duplicates could not be found
    return False

# Count frequency of elements in the list
def count_elements(nums):
    count = {}  # dictionary to store frequency
    for x in nums:
        count[x] = count.get(x, 0) + 1  # increment count
    return count

# Two Sum Template
def two_sum(nums, target):
    seen = {}  # store number → index mapping
    for i, x in enumerate(nums):
        if target - x in seen:  # found complement
            return [seen[target - x], i]
        seen[x] = i  # store current number index
    return []

'''
Problems:
    - Two Sum
    - Intersection
    - Top K Frequent
'''
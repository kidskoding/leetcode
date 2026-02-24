def twoSum(nums, target):
    # 1. Create a HashMap that pairs the numbers to their appropriate indices
    #      the numbers are keys and the indices are values
    #      the reason why this behavior is important is because to retrieve the values of a HashMap, we need the keys
    hash_map = {}
    
    # Loop through nums
    for i, x in enumerate(nums):
        # 2. Get the complement value that sums with x to equal target
        complement = target - x
        
        # 3. Check if its in the hash map
        #   If so, return the pair that sums to target. We know that the indices that pair to target
        #   will be hash_map[complement] and i
        if complement in hash_map:
            return [hash_map[complement], i]
        
        # 4. Pair an element with its index
        hash_map[x] = i
    
    # 5. Even though the problem states that there will always be a pair that sums to target,
    #   it is still good code practice to return something where there isn't a pair that sums up to
    #   target. The typical best practice in this is to return an empty array ( [] )
    return []
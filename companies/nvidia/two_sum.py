def two_sum(nums, target):
    '''
        1. Create a hash map to create a mapping between elements and their appropriate indices
        
        This will create an O(1) time complexity which will allow us 
        to easily retrieve an index for any element in our array, allowing for 
        efficient returning of the two indicies that sum to `target`
    '''
    hash_map = {}
    
    # 2. Loop through the nums array
    for i, x in enumerate(nums):
        '''
            Let complement be the difference between the target and x
            If this complement value is in the hash map, we know that it is present in 
        '''
        complement = target - x
        if complement in hash_map:
            return [i, hash_map[complement]]
    
        '''
            Add the element paired with its index to the map
        '''
        hash_map[x] = i
        
    '''
        Although mentioned that there will always be a pair that sums to target,
        its a good software convention to write what the expected
        return value of the function should be when there isn't a pair that sums to target
        
        Since the problem doesn't specify, I can just return a default empty list
    '''
    return []
def contains_duplicate(nums):
    # 1. Let seen be a set to track the distinct elements in nums that I have already seen
    seen = set()
    
    # 2. Loop through nums
    for x in nums:
        '''
            If an element (x) has been added to seen already, we know that we can
            immediately return True because a duplicate is already present in nums!
        '''
        if x in seen:
            return True
        
        '''
            Add the element (x) to our seen set so it can track the elements
            that have already been seen
        '''
        seen.add(x)
        
    '''
        If no elements repeat, meaning they don't reappear in nums when they have already been added to seen,
        then we can just return false. In this scenario, all elements are distinct
    '''
    return False
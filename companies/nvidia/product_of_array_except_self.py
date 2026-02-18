def productOfArrayExceptSelf(self, nums):
    '''
        1. Create a list that will store the product of all elements in nums
            except for nums[i], without affecting our nums array
    '''
    lst = [1] * len(nums)
    
    '''
        2. Build a prefix product where lst[i] will store the product of all elements
            from 0 to the second to last element in the list
    '''
    prefix = 1
    for i in range(len(nums)):
        lst[i] = prefix
        prefix *= nums[i]
        
    '''
        3. Modify `lst` to build a suffix product, where lst[i] will store the product of all
            elements from len(nums) - 1 back to the first index
    '''
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        # Update suffix to be product between itself and the visited element in nums
        lst[i] *= suffix
        
        '''
            Update each entry in lst to be the product of suffix

            This method works because we get the product of all values except at the current
            index by getting the prefix product (all numbers before the current index) and
            multiplying it by the suffix product (all numbers after the current index)
        '''
        suffix *= nums[i]
        
    '''
        Return the resulting list
    '''
    return lst
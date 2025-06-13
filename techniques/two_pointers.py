'''
    Given a list check if two numbers sum up
    to a given target
    
    Test Case #1:
        Sample Input:
            nums = [10, 13, 8, 6, 1, 3, 4]
            target = 13
        Sample Output:
            True (3 + 10 = 13)
    
    Test Case #2:
        Sample Input:
            nums = [10, 13, 8, 6, 1, 3, 4]
            target = 23
        Sample Output:
            True (10 + 13 = 23)
'''

def twoPointersDemo(lst, target):
    # sort the list to leverage the two pointers technique
    lst = sorted(lst)
    
    # two pointers pointing at two ends of a list
    left = 0
    right = len(lst) - 1
    
    # Loop through the pointers, eliminating the pairs that will not equal the target
    while left < right:
        # we can return true immediately if we know two elements sum to the given target
        if lst[left] + lst[right] == target:
            return True
        
        # if the sum is less than the target, we can move the left pointer by 1
        # this will effectively eliminate the pairs that will have a sum less than the target
        elif lst[left] + lst[right] < target:
            left += 1
            
        # otherwise we can move the right pointer by 1
        # this will effectively eliminate the pairs that will have a sum greater than the target
        else:
            right -= 1
            
    return False            
            
print(twoPointersDemo([10, 13, 8, 6, 1, 3, 4], 13))
print(twoPointersDemo([10, 13, 8, 6, 1, 3, 4], 23))
print(twoPointersDemo([10, 13, 8, 6, 1, 3, 4], 33))
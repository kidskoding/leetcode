from collections import Counter

def findDuplicates(nums):
    # 1. Let freq be a counter that stores the frequency of each number in nums as part of a HashMap
    freq = Counter(nums)
    
    # 2. Check through freq and see if there are any numbers occuring more than once
    #    If so, return them in a list!
    return [x for x, count in freq.items() if count > 1]
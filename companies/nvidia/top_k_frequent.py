def topKFrequent(nums, k):
    # 1. Let frequencies be a hash map to store the frequencies of each element in nums
    frequencies = {}
    
    # 2. Loop through nums and add the frequency of each element in nums to the frequencies hash map
    for x in nums:
        frequencies[x] = frequencies.get(x, 0) + 1
        
    # 3. Sort the frequencies map by its values in descending order
    frequencies = sorted(frequencies, key=lambda x: frequencies[x], reverse=True)
    
    '''
        4. Return a list of frequencies's keys up to k
    
        I already sorted frequencies in descending order by value, and
        Python's sorted function returns a list of keys in frequencies
        
        The most frequent element will be the first element in the map because I sorted the keys
        in descending order by their values!
        
        Therefore, returning all the elements in the converted list up to k
        will give the top k most frequent elements
    '''
    return frequencies[:k]
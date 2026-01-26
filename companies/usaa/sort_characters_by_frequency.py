from collections import Counter

def sort_characters_by_frequency(s):
    # Step 1: Create a HashMap that stores the frequencies of string s
    freqs = {}
    
    # Step 2: Populate the frequencies HashMap with the frequencies of string s
    for x in s:
        freqs[x] = freqs.get(x, 0) + 1
        
    # Step 3: 
    # 1. Sort the HashMap in descending order by number of characters, with the most frequent character
    # being first in the resulting list
    # 
    # 2. Use a custom comparator lambda function that will also natural sort each distinct character in ASCII
    # order
    # 
    # 3. Return the resulting sort as a list!
    lst = sorted(freqs, key=lambda x: (-freqs[x], x))
    
    # Step 4: Create a resulting string
    res = ""
    
    # Step 5: Loop through each character in the list and 
    # multiply each character by its frequency in order to get all 
    # how many times the character appeared in the original string
    for x in lst:
        res += x * freqs[x]
    
    # Step 6: Return the resulting string!
    return res
    
print(sort_characters_by_frequency('Aabb'))
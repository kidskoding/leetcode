def valid_anagram(s, t):
    # Step 1: Create a HashMap that stores the frequencies of one of the two strings (s)
    freqs = {}
    
    # Step 2: Loop through string s and add its character frequency to a HashMap
    for x in s:
        freqs[x] = freqs.get(x, 0) + 1
        
    # Step 3: Loop through the other string (t), and if a character exists in s as well, 
    # decrement its frequency count
    # 
    # This approach makes it so that when the character count is 0, we can remove 
    # the character key from the map. 
    # 
    # Anagrams occur when the frequencies of each character in both strings are equivalent.
    # Therefore, By removing character keys from the frequency map, we know an anagram exists between the two strings 
    # if the HashMap is completely empty!
    for x in t:
        # 
        if x in s:
            freqs[x] -= 1
        
            # Step 4: If there are no more occurrences of a character in the HashMap,
            # delete the key from the HashMap
            if freqs[x] == 0:
                del freqs[x]
    
    # Step 5: Return True if the length of the freqs HashMap is 0. Otherwise, return False
    return len(freqs) == 0
def areEqualOccurrences(self, s):
    # Step 1: Create a HashMap containing the frequency of each character in s
    freqs = {}
    
    # Step 2: Populate the HashMap of frequencies with String s
    for x in s:
        freqs[x] = freqs.get(x, 0) + 1
        
    # Step 3: Get the values of the frequencies map as a set
    st = set(freqs.values())
    
    # Step 4: Check if the length of the set is 1!
    # 
    # We know that if we form a set out of the values of the frequency map
    # and the frequency of each character is the same value, the set will always have a length of 1!
    return len(st) == 1
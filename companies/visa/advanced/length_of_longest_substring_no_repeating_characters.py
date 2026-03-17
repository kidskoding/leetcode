def lengthOflongestSubstringWithoutRepeatingCharacters(s):
    # 1. Let left be the left side of the sliding window
    #   Left won't change unless a certain condition is valid (in this case longest 
    #   substring without repeating characters)
    left = 0
    
    # 2. Let seen be a HashSet of characters that have already been seen in s
    seen = set()
    
    # 3. Let max_len be the length of the longest substring without repeating characters
    max_len = 0
    
    # 4. Loop through s, where right represents the end of the sliding window
    for right in range(len(s)):
        # 5. Shrink the window from the left until we find a character that hasn't been seen before
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
            
        # 6. Expand the sliding window to add s[right] to the end of the window
        seen.add(s[right])
        
        # 7. Update the maximum length
        max_len = max(max_len, right - left + 1)
    
    # 8. Return the maximum length
    return max_len
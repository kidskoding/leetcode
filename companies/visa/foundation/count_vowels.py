def countVowels(s):
    # 1. Lowercase the s to ignore case sensitivity
    s = s.lower()
    
    # 2. Let vowels be the set that stores the vowels in the english alphabet (a, e, i, o, and u)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # 3. Let count be the number of vowels there are in s
    count = 0
    
    # Loop through each character in vowels
    for x in s:
        # 4. Increment count if character x is a vowel (its present in the vowels set)
        if x in vowels:
            count += 1
        
    # 5. Return the count of vowels
    return count
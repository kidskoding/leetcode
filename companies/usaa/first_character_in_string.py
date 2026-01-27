def first_unique_char(s):
    # Step 1: Create a list to store the characters that occur once
    distinct_idxs = []
    
    # Step 2: Loop through each character in s
    for (i, x) in enumerate(s):
        # Step 3: Check if the number of times x occurs in s is equivalent to 1
        # If so, add it to the list
        if s.count(x) == 1:
            distinct_idxs.append(i)
            
    # Step 4: If the list exists, return the first indexed character, otherwise return -1
    # 
    # This approach works because we know that lists maintain insertion order, so
    # by adding the distinct characters from index 0 to len(s) - 1 to our list,
    # the first unique character will be the first character in our list
    return distinct_idxs[0] if distinct_idxs else -1

print(first_unique_char('leetcode'))
def intersect(nums1, nums2):
    # Step 1: Create a HashSet, intersection, containing the intersection of nums1 and nums2 as sets
    # However, this does not preserve the count. It is only distinct numbers
    intersection = list(set(nums1) & set(nums2))
    
    # Step 2: 
    # Create a list, occurrences, that will populate based on the number of occurrences of each element in intersection
    occurrences = []
    
    # Step 3: We know that each element in the resulting set must appear as many times as it shows in both arrays
    #
    # To do this, we can take the minimum of the counts of the elements in both lists and multiply that by the distinct 
    # element stored in intersection
    for x in intersection:
        occurrences.extend([x] * min(nums2.count(x), nums1.count(x)))
    
    # Step 4: Return the final list
    return occurrences

print(intersect([1, 2, 2, 1], [2, 2]))
from collections import defaultdict

def groupAnagrams(strs):
    ''' 
        1. Let grouped_anagrams a hash map, where a key will consist of a word
        and a value will consist of a list of all anagrams of that word that exist in strs
    '''
    grouped_anagrams = defaultdict(list)
    
    # 2. Loop through strs
    for x in strs:
        '''
            Since anagrams are formed by switching up the order of the letters,
            we need one consistent way to group all the anagrams together
            
            If I had anagrams "tan" and "nat", I would need to find a common key for 
            my HashMap that would store these two entries together as a list as apart
            of the same key in my HashMap
            
            One good technique to resolve this is to sort the current anagram
            I am trying to group. Each key will then contain a value that is a 
            sorted list of all anagrams of the key.
            
            For example, tan and nat will give me the same result if I were to sort
            their characters! I can then append these words as a part of a list of all
            anagrams of the sorted word
        '''
        grouped_anagrams[str(sorted(x))].append(x)
    
    # 3. Return a list of the grouped anagrams values
    return list(grouped_anagrams.values())
# Define the input which is strings we need strings in the array for the input
# Contract: function signature = groupAnagrams(strs: List[str]) -> List[List[str]]
# Purpose: Given an array of strings, group all anagrams together into sublists using a hash map key.
#
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hash map mapping sorted string key -> list of anagrams
        res = defaultdict(list)
        
        for s in strs:
            # Sort the characters of s to create a unique identifier
            #s = "act" = ['a','c','t'] = "act"
            #s = "cat" = ['a','c','t'] = "act"
            key = "".join(sorted(s))
           
            
            # Append the original word to the list matching that key
            res[key].append(s)
            
        # Return all accumulated lists of anagrams
        return list(res.values())
        


        
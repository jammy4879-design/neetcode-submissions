# consider that the words must both be the exact same amount and contain each letter. 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else: 
            return Counter(s) == Counter(t)
        
        
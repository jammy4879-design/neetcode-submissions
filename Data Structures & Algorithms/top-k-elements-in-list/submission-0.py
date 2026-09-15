from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Contract: topKFrequent(nums: List[int], k: int) -> List[int]
        # Purpose: Return the k most frequent elements in O(N) time using bucket sort.
        
        # 1. Count frequencies using a Hash Map (Key: num, Value: frequency)
        count = Counter(nums)
        
        # 2. Bucket array: Index represents frequency, value is list of numbers
        # Size is len(nums) + 1 because the max frequency possible is len(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        
        # 3. Populate frequency buckets from hash map items
        for num, c in count.items():
            freq[c].append(num)
            
        # 4. Gather the top k elements by iterating backwards through buckets
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
    
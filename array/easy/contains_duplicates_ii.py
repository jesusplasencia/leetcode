from typing import List;

class Solution:
    def containsNearbyDuplicateV1(self, nums: List[int], k: int) -> bool:
        dictionary = {};
        for (n, idx) in enumerate(nums):
            if n in dictionary:
                if (abs(dictionary[n] - idx) <= k):
                    return True
            dictionary[n] = idx
        return False
    
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if (len(nums) == 1 or len(nums) == len(set(nums))):
            return False
        d = {}
        for idx, num in enumerate(nums):
            if num in d and idx - d[num] <= k:
                return True
            d[num] = idx
        return False
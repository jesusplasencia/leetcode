from typing import List

# First Solution ( O(n) time complexity, O(1) space complexity )
class Solution:
    def containsDuplicateV1(self, nums: List[int]) -> bool:
        dictionary = {};
        for num in nums:
            if num in dictionary:
                return True;
            dictionary[num] = 1;
        return False;
    
# Best Solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
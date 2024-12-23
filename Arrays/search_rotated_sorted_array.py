from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        return nums.index(target)
    
    
if __name__ == "__main__":
    s = Solution()
    nums = [1]
    target = 0
    print(s.search(nums, target)) # Output: 4
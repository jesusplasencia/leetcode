from typing import List

# O(n) runtime complexity
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        c_index = 0;
        for (index, num) in enumerate(nums):
            if num == target:
                return index
            elif num > target:
                return index
            elif num < target:
                c_index = index + 1
        return c_index
    
# O(log n) runtime complexity
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2 # Get the middle index
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
    
# Test
if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,3,5,6], 5)) # 2
    print(s.searchInsert([1,3,5,6], 2)) # 1
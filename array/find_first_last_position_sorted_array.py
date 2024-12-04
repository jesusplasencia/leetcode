from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)  # Get the length of the list
        if n == 0:  # If the list is empty, return [-1, -1]
            return [-1, -1]
        
        left = 0  # Initialize left pointer
        right = n - 1  # Initialize right pointer
        
        # Find the leftmost index of target
        while left < right:  # Binary search loop
            mid = (left + right) // 2  # Calculate mid index
            if nums[mid] < target:  # If mid value is less than target
                left = mid + 1  # Move left pointer to mid + 1
            else:  # If mid value is greater than or equal to target
                right = mid  # Move right pointer to mid
        
        if nums[left] != target:  # If target is not found at left pointer
            return [-1, -1]  # Return [-1, -1]
        
        start = left  # Store the start index
        right = n - 1  # Reset right pointer
        
        # Find the rightmost index of target
        while left < right:  # Binary search loop
            mid = (left + right) // 2 + 1  # Calculate mid index, bias towards right
            if nums[mid] > target:  # If mid value is greater than target
                right = mid - 1  # Move right pointer to mid - 1
            else:  # If mid value is less than or equal to target
                left = mid  # Move left pointer to mid
        
        return [start, right]  # Return the start and end indices of the target range
    
    
if __name__ == "__main__":
    s = Solution()
    nums = [1]
    target = 1
    print(s.searchRange(nums, target))
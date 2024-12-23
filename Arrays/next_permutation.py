from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        
        # Find the largest index i such that arr[i] < arr[i+1]
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # Index found, swap and reverse
        if i >= 0:
            j = n - 1
            
            # Find the largest index j such that arr[i] < arr[j]
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            
            # Swap arr[i] and arr[j]
            nums[i], nums[j] = nums[j], nums[i]
        
        # Reverse the sublist arr[start:end+1]
        rev(nums, i+1, n-1)
        
def rev(nums, start, end):
    while start < end:
        swap(nums, start, end)
        start += 1
        end -= 1
        
def swap(arr: list, i: int, j: int) -> None:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
if __name__ == "__main__":
    s = Solution()
    nums = [3, 2, 1]
    s.nextPermutation(nums)
    print(nums)
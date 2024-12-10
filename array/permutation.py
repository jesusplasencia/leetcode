from typing import List
import math

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        iteration = math.factorial(n)
        result = []
        
        for _ in range(iteration):
            self.nextPermutation(nums)
            result.append(nums[:])
            
        return result
    
    
    def nextPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        rev(nums, i + 1, n - 1) 
    
def rev(nums, start, end):
    while start < end:
        swap(nums, start, end)
        start += 1
        end -= 1
        
def swap(arr: list, i: int, j: int) -> None:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
    
# Time complexity: O(n!)
# Space complexity: O(n!)
# where n is the length of the input list nums
if __name__ == "__main__":
    s = Solution();
    nums = [1, 2, 3]
    print(s.permute(nums)) # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
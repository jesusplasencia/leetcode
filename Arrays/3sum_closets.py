from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        for i in range(len(nums) - 2): #Iterate through the list
            if i > 0 and nums[i] == nums[i - 1]: #Avoid to process the same number
                continue
            l, r = i + 1, len(nums) - 1 #Two pointers
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(closest_sum - target):
                    closest_sum = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s
        return closest_sum
    

if __name__ == "__main__":
    s = Solution();
    nums = [-4,2,2,3,3,3];
    target = 0;
    print(s.threeSumClosest(nums, target));
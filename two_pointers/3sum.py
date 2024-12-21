from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if nums[i] > 0: break;
            if i > 0 and nums[i] == nums[i - 1]: continue;
            lo, hi = i + 1, n - 1
            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi];
                if summ == 0:
                    res.append([nums[i], nums[lo], nums[hi]]);
                    while lo < hi and nums[lo] == nums[lo - 1]: lo += 1;
                    while lo < hi and nums[hi] == nums[hi + 1]: hi -= 1;
                elif summ < 0:
                    lo += 1;
                else:
                    hi -= 1;
        return res;
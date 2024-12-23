from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in s:
                next_num = num + 1
                length = 1
                while next_num in s:
                    length += 1
                    next_num += 1
                longest = max(longest, length)
        return longest
    
if __name__ == "__main__":
    sol = Solution();
    nums = [1,2,0,1];
    res = sol.longestConsecutive(nums);
    print(res);
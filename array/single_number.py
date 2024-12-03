from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a ^= num
        return a

if __name__ == "__main__":
    s = Solution();
    nums = [2, 2, 1];
    print(s.singleNumber(nums)); # 1
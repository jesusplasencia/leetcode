from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0;
        dictionary = {};
        for (index, num) in enumerate(nums):
            if num not in dictionary:
                dictionary[num] = True;
                nums[count] = num;
                count += 1;
        return count;


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2])) # 2
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {};
        for (index, num) in enumerate(nums):
            if (target - num) in dictionary:
                return [dictionary[target - num], index];
            dictionary[num] = index;
        return [0, 0]; #default return


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))

    print(s.twoSum([3,2,4], 6))

    print(s.twoSum([-1,0], -1))
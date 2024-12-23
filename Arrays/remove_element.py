from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0;
        for (index, num) in enumerate(nums):
            if num != val:
                nums[count] = num;
                count += 1;
        return count;


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3,2,2,3], 3)) # 2
    print(s.removeElement([0,1,2,2,3,0,4,2], 2)) # 5
    print(s.removeElement([3,3], 3)) # 0
    print(s.removeElement([3,3], 5)) # 2
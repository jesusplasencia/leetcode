from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2;
        nums.sort();
        size = len(nums);
        if (size % 2 == 1):
            return (float(nums[size // 2]));
        else:
            return (float(nums[size // 2 - 1] + nums[size // 2]) / 2);

if __name__ == "__main__":
    s = Solution();
    nums1 = [1, 2];
    nums2 = [3, 4];
    print(s.findMedianSortedArrays(nums1, nums2)); # 2.5
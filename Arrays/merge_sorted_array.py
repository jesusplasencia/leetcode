from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if (len(nums2) == 0): return;

        temp = [0] * (m);
        for p in range(m):
            temp[p] = nums1[p];
        
        i, j = 0, 0;
        for k in range(m + n):
            if (i >= m):
                nums1[k] = nums2[j];
                j += 1;
            elif (j >= n):
                nums1[k] = temp[i];
                i += 1;
            elif (temp[i] < nums2[j]):
                nums1[k] = temp[i];
                i += 1;
            else:
                nums1[k] = nums2[j];
                j += 1;


if __name__ == "__main__":
    s = Solution();
    nums1 = [1, 2, 3, 0, 0, 0];
    m = 3;
    nums2 = [2, 5, 6];
    n = 3;
    s.merge(nums1, m, nums2, n);
    print(nums1); # [1, 2, 2, 3, 5, 6]
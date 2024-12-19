from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1;
        max_area = 0;
        while (i < j):
            w = j - i
            h = min(height[j], height[i])
            a = h * w
            max_area = max(max_area, a)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return max_area;
    
if __name__ == "__main__":
    s = Solution()
    heights = [1,2,1]
    print(s.maxArea(heights))
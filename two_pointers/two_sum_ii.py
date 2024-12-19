from typing import List;

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while (i < j):
            currSum = numbers[i] + numbers[j]
            if (currSum == target): break;
            elif (currSum > target): j -= 1;
            else: i += 1;
        return [i + 1, j + 1];
    
if __name__ == "__main__":
    s = Solution();
    numbers = [5,25,75]
    target = 100
    print(s.twoSum(numbers, target));
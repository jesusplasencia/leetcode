from typing import List

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         carry = 1
#         for i in range(len(digits) - 1, -1, -1):
#             if carry == 0:
#                 break
#             digits[i] += carry # Add the carry to the current digit
#             carry = digits[i] // 10 # Get the carry (e.g. 9 + 1 = 10, carry = 1)
#             digits[i] %= 10 # Get the remainder
#         if carry:
#             digits.insert(0, carry) # Insert 1 at the beginning of the list
#         return digits

# O(n) runtime complexity (From array to string)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''.join(map(str, digits))
        num1 = int(string) + 1
        return [int(num) for num in str(num1)]
    
# Test Cases
if __name__ == "__main__" :
    s = Solution()
    print(s.plusOne([1, 2, 3])) # Expected Output: [1, 2, 4]
    print(s.plusOne([4, 3, 2, 1])) # Expected Output: [4, 3, 2, 2]
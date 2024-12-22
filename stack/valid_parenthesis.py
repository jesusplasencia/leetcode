class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()")) # True
    # print(s.isValid("()[]{}")) # True
    # print(s.isValid("(]")) # False
    # print(s.isValid("([)]")) # False
    # print(s.isValid("{[]}")) # True
    # print(s.isValid("{{}")) # False
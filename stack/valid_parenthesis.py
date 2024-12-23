class Solution:
    def isValid(self, s: str) -> bool:
        stk = [];
        for c in s:
            if not stk:
                stk.append(c);
            else:
                if (self.isClosure(stk[-1], c)):
                    stk.pop();
                else:
                    stk.append(c);
        return len(stk) == 0;

    def isClosure(self, prev, curr):
        if (prev == "{" and curr == "}"): return True;
        elif (prev == "[" and curr == "]"): return True;
        elif (prev == "(" and curr == ")"): return True;
        return False;

if __name__ == '__main__':
    s = Solution()
    print(s.isValid("([)]"));       # False
    print(s.isValid("()"));         # True
    print(s.isValid("()[]{}"));     # True
    print(s.isValid("(]"));         # False
    print(s.isValid("([])"));       # True
    print(s.isValid("(){}}{"));     # False
    print(s.isValid("({[)"));       # False
    
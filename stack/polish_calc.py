from typing import List;
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = [];
        for token in tokens:
            if token in ["+", "-", "*", "/"] and len(stk) >= 2: # Avoid empty stack
                num2 = stk.pop();
                num1 = stk.pop();
                if token == "+":
                    stk.append(num1 + num2);
                elif token == "-":
                    stk.append(num1 - num2);
                elif token == "*":
                    stk.append(num1 * num2);
                elif token == "/":
                    stk.append(int(num1 / num2));
            else:
                stk.append(int(token));
        return stk.pop();

if __name__ == "__main__":
    sol = Solution();
    print(sol.evalRPN(["2", "1", "+", "3", "*"])); # 9
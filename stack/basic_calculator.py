class Solution:
    def calculate(self, s: str) -> int:
        output,curr,sign,stk = 0,0,1,[]
        for c in s:
            if c.isdigit():
                curr = curr*10 + int(c);
            elif c in "+-":
                output += (curr*sign);
                curr = 0;
                if c == "+":
                    sign = 1;
                else:
                    sign = -1;
            elif c == "(":
                stk.append(output);
                stk.append(sign);
                output = 0;
                sign = 1;
            elif c == ")":
                output += (curr*sign);
                output *= stk.pop();
                output += stk.pop();
                curr = 0;
        return output + (curr * sign);

if __name__ == "__main__":
    sol = Solution();
    print(sol.calculate("(1+(4+5+2)-3)+(6+8)"));
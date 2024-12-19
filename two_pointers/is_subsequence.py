class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if (len(s) == 0): return True;
        if (len(s) == len(t) or len(t) == 0): return False;
        j = 0
        for i in range(len(t)):
            if (j == len(s)): return True;
            letter_to_found = s[j];
            if (t[i] == letter_to_found): j += 1
        
        return j == len(s);

if __name__ == "__main__":
    sol = Solution();
    s = "b";
    t = "abc";
    res = print(sol.isSubsequence(s, t))
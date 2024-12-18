class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1;
        while (i < j):
            if not s[i].isalnum(): i += 1; continue;
            if not s[j].isalnum(): j -= 1; continue;
            left, right = s[i].upper(), s[j].upper()
            if (left != right): return False;
            i += 1;
            j -= 1;
        return True
        

if __name__ == "__main__":
    sol = Solution();
    s = "0P";
    print(sol.isPalindrome(s))
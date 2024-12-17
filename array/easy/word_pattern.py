class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if (len(list(pattern)) != len(s.split(" "))): return False;
        d = {}
        b = {}
        s = s.split(" ")
        for (idx, letter) in enumerate(list(pattern)):
            if ((letter in d and d[letter] != s[idx]) or (s[idx] in b and b[s[idx]] != letter)): return False
            d[letter] = s[idx]
            b[s[idx]] = letter
        return True
    
if __name__ == "__main__":
    sol = Solution()
    pattern = "abba"
    s = "dog cat cat dog"
    res = sol.wordPattern(pattern, s)
    print(res)
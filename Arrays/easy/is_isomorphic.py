from collections import Counter;

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)): return False;
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False;
            else:
                d[s[i]] = t[i]
        return True;
    
    
if __name__ == "__main__":
    s = Solution()
    s1 = "bbbaaaba"
    s2 = "aaabbbba"
    #res = s.isIsomorphic(s1, s2)
    res = set("baba")
    print(res)
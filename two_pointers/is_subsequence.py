class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, len(t)
        res = ""
        while (i < j):
            if (t[i] in s): res = res + t[i]
            i += 1
        print('res:', res)
        return s == res

if __name__ == "__main__":
    sol = Solution();
    s = "abc";
    t = "ahbgdc";
    res = print(sol.isSubsequence(s, t))
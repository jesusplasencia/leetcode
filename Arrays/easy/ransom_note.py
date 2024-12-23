from collections import Counter;

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        for val in c1.keys():
            if (c1[val] > c2[val]):
                return False
        return True
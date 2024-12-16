from typing import List;
from collections import Counter;

class Solution:
    def isAnagramV1(self, s: str, t: str) -> bool:
        c1 = Counter(s);
        c2 = Counter(t);
        return c1 == c2;

    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False;
        for letter in set(s):
            if (s.count(letter) != t.count(letter)):
                return False;
        return True;
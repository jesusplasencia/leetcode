from typing import List;
from collections import Counter;

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c1 = Counter(nums);
        n = len(c1.keys())
        return c1.keys()[n-k:n];
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]] # first row
        for i in range(1, numRows):
            res.append([1])
            for j in range(1, i):
                res[i].append(res[i-1][j-1] + res[i-1][j])
            res[i].append(1)
        return res
    
if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        res = [[1]] # first row
        for i in range(1, rowIndex + 1):
            res.append([1])
            for j in range(1, i):
                res[i].append(res[i-1][j-1] + res[i-1][j])
            res[i].append(1)
        return res[rowIndex]
    

if __name__ == '__main__':
    s = Solution()
    print(s.getRow(3)) # [1,3,3,1]
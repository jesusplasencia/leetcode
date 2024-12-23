from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        setMap = {
            "row":[set() for _ in range(9)], # create a list of 9 sets
            "col":[set() for _ in range(9)], # create a list of 9 sets
            "sq":[set() for _ in range(9)]   # create a list of 9 sets
        }
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    if num in setMap["row"][i]: return False
                    else: setMap["row"][i].add(num)
                    if num in setMap["col"][j]: return False
                    else: setMap["col"][j].add(num)
                    square = (i//3*3+j//3) # calculate the square number
                    if num in setMap["sq"][square]: return False
                    else: setMap["sq"][square].add(num)
        return True
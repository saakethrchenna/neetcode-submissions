class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)],[set() for _ in range(3)],[set() for _ in range(3)]]
        for i in range(len(board)):
            for e in range(len(board)):
                val = board[i][e]
                if val in rows[i] or val in cols[e] or val in squares[i//3][e//3]:
                    return False
                if val != ".":
                    rows[i].add(val)
                    cols[e].add(val)
                    squares[i//3][e//3].add(val)
        return True
        
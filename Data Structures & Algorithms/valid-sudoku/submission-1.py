class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nrows = len(board)
        ncols = len(board[0])

        colcheck = defaultdict(set)
        rowcheck = defaultdict(set)
        squarecheck = defaultdict(set)

        for r in range(nrows):
            for c in range(ncols):
                v = board[r][c]
                if v == ".":  # skip all the non numbers
                    continue

                if v in colcheck[c] or v in rowcheck[r] or v in squarecheck[(r // 3, c // 3)]:
                    return False

                colcheck[c].add(v)
                rowcheck[r].add(v)
                squarecheck[(r // 3, c // 3)].add(v)

        return True

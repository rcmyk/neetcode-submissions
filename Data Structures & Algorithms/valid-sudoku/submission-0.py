class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            uniq = set()
            cnt = 0
            for c in row:
                if c != '.':
                    uniq.add(c)
                    cnt += 1
            if len(uniq) < cnt:
                return False
        for j in range(len(board[0])): # all are same sized
            uniq = set()
            cnt = 0
            for i in range(len(board)):
                if board[i][j] != '.':
                    uniq.add(board[i][j])
                    cnt += 1
            if len(uniq) < cnt:
                return False
        
        for i in range(len(board)//3):
            for j in range(len(board[0])//3):
                uniq = set()
                cnt = 0
                for ii in range(3):
                    for jj in range(3):
                        r = i * 3 + ii
                        c = j * 3 + jj
                        if board[r][c] != '.':
                            uniq.add(board[r][c])
                            cnt += 1
                if len(uniq) < cnt:
                    return False
                    
        return True



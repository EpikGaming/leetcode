class Solution:
    def solveSudoku(self, board: list):
        def traceback(now_board: list, i: int, j: int):
            if j == 9:
                return traceback(now_board, i + 1, 0)
            if i == 9:
                print(now_board)
                return True
            if board[i][j] != ".":
                return traceback(now_board, i, j + 1)

            for ch in range(1, 10):
                if not isValid(now_board, i, j, str(ch)):
                    continue
                board[i][j] = str(ch)
                if traceback(now_board, i, j + 1):
                    return True
                board[i][j] = "."
            return False

        def isValid(now_board: list, r: int, c: int, ch: str):
            for i in range(9):
                if now_board[r][i] == ch:
                    return False
                if now_board[i][c] == ch:
                    return False
                if now_board[int(r / 3) * 3 + int(i / 3)][int(c / 3) * 3 + (i % 3)] == ch:
                    return False
            return True

        traceback(board, 0, 0)

s = Solution()
test = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(s.solveSudoku(test))
import collections
class Solution:
    def isValidSudoku(self, board: list):
        dic = collections.defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in dic['i' + str(i)]:
                    dic['i' + str(i)].append(board[i][j])
                else:
                    return False
                if board[i][j] not in dic['j' + str(j)]:
                    dic['j' + str(j)].append(board[i][j])
                else:
                    return False
                if board[i][j] not in dic['box' + str((i // 3) * 3 + (j // 3))]:
                    dic['box' + str((i // 3) * 3 + (j // 3))].append(board[i][j])
                else:
                    return False
        return dic

s = Solution()
test = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

print(s.isValidSudoku(test))
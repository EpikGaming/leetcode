import collections
class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.word = ""

    def insert(self, word: str):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word


class Solution:
    def findWord(self, board: list, words: list):
        res = set()
        trie = Trie()
        m = len(board)
        n = len(board[0])

        for word in words:
            trie.insert(word)

        def dfs(now: Trie, i1: int, j1: int):
            if board[i1][j1] not in now.children:
                return

            ch = board[i1][j1]
            now = now.children[ch]
            if now.word != "":
                res.add(now.word)

            board[i1][j1] = "#"
            for i2, j2 in [(i1 + 1, j1), (i1, j1 + 1), (i1 - 1, j1), (i1, j1 - 1)]:
                if 0 <= i2 < m and 0 <= j2 < n:
                    dfs(now, i2, j2)
            board[i1][j1] = ch

        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)
        return list(res)

s = Solution()
test = [['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']]
word = ['oath', 'pea', 'eat', 'rain']
print(s.findWord(test, word))
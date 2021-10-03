class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str):
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def searchPrefix(self, prefix: str):
        node = self
        for ch in prefix:
            ch = ord(ch) - ord('a')
            if not self.children[ch]:
                return None
            node = node.children[ch]
        return node

    def search(self, words: str):
        node = self.searchPrefix(words)
        return node is not None and self.isEnd

    def startsWith(self, prefix: str):
        return self.searchPrefix(prefix) is not None
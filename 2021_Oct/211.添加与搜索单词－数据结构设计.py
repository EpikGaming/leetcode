"""
请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
实现词典类 WordDictionary ：
WordDictionary() 初始化词典对象
void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
bool search(word) 如果数据结构中存在字符串与word 匹配，则返回 true ；
否则，返回 false 。word 中可能包含一些 '.' ，每个. 都可以表示任何一个字母。
"""
"""
字典树＋深搜
如果遇到非"."字符，则遍历该节点对应字符的child节点，否则，遍历这一个节点的全部child
"""
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

    def insert(self, word: str):
        node = self
        for ch in word:
            c = ord(ch) - ord('a')
            if not node.children[c]:
                node.children[c] = Trie()
            node = node.children[c]
        node.isWord = True

class WordDictionary:
    def __init__(self):
        self.trieRoot = Trie()

    def addWord(self, word: str):
        self.trieRoot.insert(word)

    def search(self, word: str):
        def dfs(index: int, node: Trie):
            if index == len(word):
                return node.isWord
            ch = word[index]
            if ch != ".":
                child = node.children[ord(ch) - ord('a')]
                if child is not None and dfs(index + 1, child):
                    return True
            else:
                for child in node.children:
                    if child is not None and dfs(index + 1, child):
                        return True
            return False

        return dfs(0, self.trieRoot)

s = WordDictionary()
s.addWord("pad")
s.addWord("bab")
print(s.search(""))
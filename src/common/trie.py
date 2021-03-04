'''
前缀树
哈希树的变种
常用语文本词频统计
'''
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = '#'

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word:
            return False
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self.end_of_word in node

    def startsWith(self, prefix: str) -> bool:
        """ en prefix.
        """
        if not prefix:
            return False
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True

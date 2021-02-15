'''
208. 实现 Trie (前缀树)
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

'''


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root={}
        self.end_of_word = '#'

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return 
        node = self.root
        for c in word:
            node = node.setdefault(c,{})
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


if __name__ == '__main__':
    trie  = Trie()
    print('insert apple',trie.insert("apple"))
    print('search apple',trie.search("apple"))
    print('search app',trie.search("app"))
    print(trie.startsWith("app"))
    print(trie.startsWith("1app"))

    print('insert app', trie.insert("app"))
    print('search app',trie.search("app"))


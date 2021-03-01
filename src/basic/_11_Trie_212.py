'''
212. 单词搜索 II
给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例 1：

输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
输出：["eat","oath"]
示例 2：


输入：board = [["a","b"],["c","d"]], words = ["abcb"]
输出：[]
 

提示：

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] 是一个小写英文字母
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] 由小写英文字母组成
words 中的所有字符串互不相同
'''



class Solution:

    # 左右上下
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dx_y = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
    ]
    end_of_word = '#'
    def dfs(self, board, row, col, cur_word, cur_dict):
        cur_word += board[row][col]
        cur_dict = cur_dict[board[row][col]]

        if self.end_of_word in cur_dict:
            self.result.add(cur_word)

        tmp, board[row][col] = board[row][col], '@'
        for i in range(4):
            x, y = self.dx[i]+row, self.dy[i]+col
            if 0 <= x < self.row_lines and 0 <= y < self.col_lines\
                    and board[x][y] != '@' and board[x][y] in cur_dict:
                self.dfs(board, x, y, cur_word, cur_dict)
        board[row][col] = tmp

    def findWords(self, board, words):
        
        if not board or not board[0] or not words:
            return []

        self.result = set()
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node[self.end_of_word] = self.end_of_word

        self.col_lines, self.row_lines = len(board[0]), len(board)

        for row in range(self.row_lines):
            for col in range(self.col_lines):
                if board[row][col] in root:
                    self.dfs(board, row, col, '', root)
        return list(self.result)


if __name__ == '__main__':
    s = Solution()
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    words = ["oath", "pea", "eat", "rain"]
    print('1', s.findWords(board, words))
    board = [["a", "b"], ["c", "d"]]
    words = ["abcb"]
    print('1', s.findWords(board, words))

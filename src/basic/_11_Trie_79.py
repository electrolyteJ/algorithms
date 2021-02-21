'''
79. 单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
 

提示：

board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

'''

directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]
class Solution:
    def check(self, board, row, col, k, word):
        if board[row][col] != word[k]:
            return False
        if k == len(word)-1:
            return True
        # self.visited.add((row,col))
        tmp, board[row][col] = board[row][col], '@'
        ret= False
        for dx,dy in directions:
            x , y = row+dx,col+dy
            if 0 <= x < self.m and 0 <= y < self.n \
                and board[x][y] != '@' \
                and self.check(board, x, y, k+1, word):
                ret = True
                # and (x, y) not in self.visited  \
                break
        board[row][col] = tmp
        # self.visited.remove((row,col))
        return ret

    def exist(self, board, word: str) -> bool:
        if not board or not board[0] or not word:
            return False
        self.m = len(board)
        self.n = len(board[0])
        # self.visited =set()
        for i in range(self.m):
            for j in range(self.n):
                if self.check(board, i, j, 0, word):
                    return True
        return False




if __name__ == '__main__':
    s = Solution()
    board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    print('1', s.exist(board, word))
    word = "SEE"
    print('1', s.exist(board, word))
    word = "ABCB"
    print('1', s.exist(board, word))

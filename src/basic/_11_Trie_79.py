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
class Solution:
    def exist(self, board, word: str) -> bool:
        if not board or not board[0] or not word:return False
        def check(row, col, k):
            if board[row][col] != word[k]:return False
            if k == len(word)-1:return True
            # self.visited.add((row,col))
            tmp, board[row][col] = board[row][col], '@'
            ret = False
            for d in range(4):
                nr, nc = row+dr[d], col+dc[d]
                if 0 <= nr < m and 0 <= nc < n \
                        and board[nr][nc] != '@' \
                        and check(nr, nc, k+1):
                    ret = True
                    # and (x, y) not in self.visited  \
                    break
            board[row][col] = tmp
            # self.visited.remove((row,col))
            return ret
        m,n = len(board),len(board[0])
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        # self.visited =set()
        #时间复杂度O(m*n*3^l)
        for i in range(m):
            for j in range(n):
                if check(i, j, 0):
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

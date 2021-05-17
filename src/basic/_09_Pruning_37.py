'''
37. 解数独
编写一个程序，通过填充空格来解决数独问题。
一个数独的解法需遵循如下规则：
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。
一个数独。
答案被标成红色。
提示：
给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。
'''
class Solution:
    def isValid(self, board, row, col, c):
        for i in range(0, 9):
            if board[i][col] != '.' and board[i][col] == c:
                return False
            if board[row][i] != '.' and board[row][i] == c:
                return False
            a = 3*(row//3)+i//3
            b = 3*(col//3)+i % 3
            if board[a][b] != '.' and board[a][b] == c:
                return False
        return True

    def solve(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != '.':
                    continue
                for c in range(1, 10):
                    if not self.isValid(board, row, col, str(c)):
                        continue
                    board[row][col] = str(c)
                    if self.solve(board):
                        return True
                    else:
                        board[row][col] = '.'
                return False
        return True

    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        #由于这些方法均以递归 + 回溯为基础，算法运行的时间（以及时间复杂度）很大程度取决于给定的输入数据，
        # 而我们很难找到一个非常精确的渐进紧界。因此这里只给出一个较为宽松的渐进复杂度上界 O(9 ^ {9*9})，
        #即最多有 9×9 个空白格，每个格子可以填[1, 9]中的任意整数。
        if not board:
            return
        self.solve(board)

if __name__ == "__main__":
    s = Solution()
    l = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    s.solveSudoku(l)
    print('1', l)

'''
51. N 皇后
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例 1：


输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：[["Q"]]
'''


class Solution:
    def solveNQueens1(self, n: int):  # 基于集合的回溯
        # 时间复杂度：O(N!)，空间复杂度：O(N)
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        solutions = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n
        backtrack(0)
        return solutions

    def solveNQueens2(self, n: int):  # 基于位运算的回溯
        # 时间复杂度：O(N!)，空间复杂度：O(N)
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def solve(row: int, columns: int, diagonals1: int, diagonals2: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                availablePositions = (
                    (1 << n) - 1) & (~(columns | diagonals1 | diagonals2))
                while availablePositions:
                    position = availablePositions & (-availablePositions)
                    availablePositions = availablePositions & (
                        availablePositions - 1)
                    column = bin(position - 1).count("1")
                    queens[row] = column
                    solve(row + 1, columns | position, (diagonals1 |
                                                        position) << 1, (diagonals2 | position) >> 1)

        solutions = list()
        queens = [-1] * n
        row = ["."] * n
        solve(0, 0, 0, 0)
        return solutions

    def solveNQueens3(self, n: int):  # 剪枝
        def gen_result(n):
            board = []
            for res in self.result:
                for i in res:
                    board.append('.'*i+'Q'+'.'*(n-i-1))
            return [board[i:i+n] for i in range(0, len(board), n)]

        def dfs(n, row, cur_state):
            if row >= n:
                self.result.append(cur_state)
                return
            for col in range(n):
                if col in self.cols or (row+col in self.pie) or (row - col in self.na):
                    continue
                self.cols.add(col)
                self.pie.add(row+col)
                self.na.add(row-col)
                dfs(n, row+1, cur_state+[col])
                self.cols.remove(col)
                self.pie.remove(row+col)
                self.na.remove(row-col)
        if n < 1:return []
        self.result = []
        self.cols = set()
        self.pie = set()
        self.na = set()
        dfs(n, 0, [])
        return gen_result(n)


if __name__ == "__main__":
    s = Solution()
    n = 4
    print("n:%s" % n)
    print('1', s.solveNQueens1(n))
    print('2', s.solveNQueens2(n))
    print('3', s.solveNQueens3(n))
    n = 1
    print("n:%s" % n)
    print('1', s.solveNQueens1(n))
    print('2', s.solveNQueens2(n))
    print('3', s.solveNQueens3(n))

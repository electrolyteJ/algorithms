'''
52. N皇后 II
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
示例 1：
输入：n = 4
输出：2
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：
输入：n = 1
输出：1
'''
class Solution:
    def dfs(self, n, row, cur_state):
        if row >= n:
            self.result.append(cur_state)
            return
        for col in range(n):
            if col in self.cols or (row+col in self.pei) or (row-col in self.na):
                continue
            self.cols.add(col)
            self.pei.add(row+col)
            self.na.add(row-col)
            self.dfs(n, row+1, cur_state+[col])
            self.cols.remove(col)
            self.pei.remove(row+col)
            self.na.remove(row-col)

    def totalNQueens1(self, n: int) -> int:
        if n < 1:
            return 0
        self.result = []
        self.cols = set()
        self.pei = set()
        self.na = set()
        self.dfs(n, 0, [])
        return len(self.result)

    def totalNQueens2(self, n: int) -> int:
        def dfs(n, row, col, pei, na):
            if row >= n:
                self.count += 1
                return
            #
            bits = (~(col | pei | na)) & ((1 << n) - 1)
            print(bin(bits))
            while bits > 0:
                p = bits & -bits  # 清除所有1仅仅保留最低位1
                print(bin(col), bin(p) ,bin(col | p))
                print(bin(pei), bin(p) ,bin((pei | p)<<1))
                print(bin(na), bin(p) ,bin((na | p)>>1))
                print("="*10)
                dfs(n, row+1, col | p, (pei | p) << 1, (na | p) >> 1)
                bits &= (bits-1)  # 清除最低位的1

        if n < 1:
            return 0
        self.count = 0
        dfs(n, 0, 0, 0, 0)
        return self.count


if __name__ == "__main__":
    s = Solution()
    print('1', s.totalNQueens1(4))
    print('2', s.totalNQueens2(4))

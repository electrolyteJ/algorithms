'''
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
'''


class Solution:
    def gen(self, left, right, n, s):
        if left == n and right == n:
            self.ret.append(s)
            return
        if left < n:
            self.gen(left+1, right, n, s+'(')
        if right < left and right < n:
            self.gen(left, right+1, n, s+')')

    def generateParenthesis1(self, n: int):
        self.ret = []
        self.gen(0, 0, n, '')
        return self.ret


if __name__ == "__main__":
    s = Solution()
    print('1', s.generateParenthesis1(3))

    print('1', s.generateParenthesis1(1))

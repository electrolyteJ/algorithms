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

    def generateParenthesis1(self, n: int):#回溯
        self.ret = []
        self.gen(0, 0, n, '')
        return self.ret
    def generateParenthesis2(self, n: int):#回溯
        def backtrack(l,r):
            nonlocal ret,visited
            if len(visited) == 2*n:
                ret.append(''.join(visited))
                return
            if l < n :
                visited.append('(')
                backtrack(l+1, r)
                visited.pop()
            if r < l:
                visited.append(')')
                backtrack(l, r+1)
                visited.pop()

        ret,visited =[],[]
        backtrack(0, 0)
        return ret
if __name__ == "__main__":
    s = Solution()
    print('1', s.generateParenthesis1(3))
    print('2', s.generateParenthesis2(3))
    print('1', s.generateParenthesis1(1))
    print('2', s.generateParenthesis2(1))

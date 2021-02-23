'''
509. 斐波那契数
斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给你 n ，请计算 F(n) 。

 

示例 1：

输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1
示例 2：

输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2
示例 3：

输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3
 

提示：

0 <= n <= 30

'''


class Solution:
    def fib1(self, n: int) -> int:  # 递归
        # 时间复杂度O(2^N)
        return n if n <= 1 else self.fib1(n-1)+self.fib1(n-2)

    def fib2(self, n):  # 递归 + 记忆化
        # 时间复杂度O(N)
        def fib(n, meno):
            if n <= 1:
                return n
            if not meno[n]:
                meno[n] = fib(n-1, meno)+fib(n-2, meno)
            return meno[n]

        return fib(n, [None]*(n+1))

    def fib3(self, n):  # dp
        # 时间复杂度O(n) 空间复杂度O(n)
        if n <= 1:
            return n
        f = [None]*(n+1)
        f[0] = 0
        f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n]

    def fib4(self, n):  # dp
        # 时间复杂度O(n) 空间复杂度O(1)
        if n <= 1:
            return n
        o, p, q, = 0, 1, 1
        for i in range(2, n):
            p, o = q, p
            q = p+o
        return q


if __name__ == '__main__':
    s = Solution()
    n = 2
    print('1', s.fib1(n))
    print('2', s.fib2(n))
    print('3', s.fib3(n))
    print('4', s.fib4(n))
    n = 3
    print('1', s.fib1(n))
    print('2', s.fib2(n))
    print('3', s.fib3(n))
    print('4', s.fib4(n))
    n = 4
    print('1', s.fib1(n))
    print('2', s.fib2(n))
    print('3', s.fib3(n))
    print('4', s.fib4(n))

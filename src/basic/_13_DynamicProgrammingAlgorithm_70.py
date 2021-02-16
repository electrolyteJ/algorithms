'''
70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''


class Solution:
    def climbStairs1(self, n: int) -> int:
        if n <=2:
            return n
        o,p,q=1,2,3
        #前三个都是已知,
        #n=1, 2，3
        #从3开始算,如果n=10，则计算 3，4，5，6，7，8，9
        for i in range(3,n):
            p,o=q,p
            q = p+o
        return q
    def climbStairs2(self, n: int) -> int:
        x, y =1,2
        for _ in range(2, n):
            x,y = y,x+y
        return y

 
if __name__=='__main__':
    s = Solution()
    n =2
    print("1",s.climbStairs1(n))
    print("2",s.climbStairs2(n))
    n =3
    print("1",s.climbStairs1(n))
    print("2",s.climbStairs2(n))

'''
647. 回文子串
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

 

示例 1：

输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
 

提示：

输入的字符串长度不会超过 1000 。

'''


class Solution:
    def countSubstrings1(self, s: str) -> int:#dp
        #时间复杂度O(n^2) 空间复杂度O(n)
        counter = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for l in range(n):
            for i in range(n):
                j = l+i
                if j >= n:
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
                if dp[i][j]:
                    counter += 1
        return counter

    def countSubstrings2(self, s: str) -> int:#中心扩散法
        #时间复杂度O(n^2) 空间复杂度O(1)
if __name__ =='__main__':
    ss = Solution()
    s = "abc"
    print('1',ss.countSubstrings1(s))
    s = "aaa"
    print('1',ss.countSubstrings1(s))



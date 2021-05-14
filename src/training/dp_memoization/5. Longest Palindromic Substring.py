'''
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。
示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：
输入：s = "cbbd"
输出："bb"
示例 3：
输入：s = "a"
输出："a"
示例 4：`

输入：s = "ac"
输出："a"
提示：

1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成

'''
class Solution:
    def longestPalindrome1(self, s: str) -> str:#dp
        #时间复杂度O(n^2) 空间复杂度O(n)
        n =len(s)   
        dp = [[False]*n for _ in range(n)]
        ret = ''
        for gap in range(n):
            for i in range(n):
                j = gap+i
                if j >= n:
                    break
                if gap==0:
                    dp[i][j]=True
                elif gap == 1:
                    dp[i][j]=(s[i]==s[j])
                else:
                    dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
                if dp[i][j] and gap+1 > len(ret):
                    ret = s[i:j+1]
        return ret
    def longestPalindrome2(self, s: str) -> str:#中心扩散法
        #时间复杂度O(n^2) 空间复杂度O(n)  
        pass
                
                    

        pass
if __name__ =='__main__':
    ss = Solution()
    s = "babad"
    print('1', ss.longestPalindrome1(s))
    print('2', ss.longestPalindrome2(s))
    s = "cbbd"
    print('1', ss.longestPalindrome1(s))
    print('2', ss.longestPalindrome2(s))
    s = "a"
    print('1', ss.longestPalindrome1(s))
    print('2', ss.longestPalindrome2(s))
    s = "ac"
    print('1', ss.longestPalindrome1(s))
    print('2', ss.longestPalindrome2(s))

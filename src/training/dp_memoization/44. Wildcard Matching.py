'''
44. 通配符匹配
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输出: false
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:  # dp
        m, n = len(s), len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = True
            else:
                break
        # 时间复杂度O(mn) 空间复杂度O(mn)
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif p[j-1] == '?' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]

    def isMatch2(self, s: str, p: str) -> bool:  # greedy
        #时间复杂度O(mn) 空间复杂度O(1)
        sRight, pRight = len(s), len(p)
        while sRight > 0 and pRight > 0 and p[pRight-1] != '*':
            if s[sRight-1] == p[pRight-1] or p[pRight-1] == '?':
                sRight -= 1
                pRight -= 1
            else:
                return False
        if pRight == 0:
            return sRight == 0
        sIndex, pIndex = 0, 0
        sRecord, pRecord = -1, -1
        while sIndex < sRight and pIndex < pRight:
            if p[pIndex] == '*':
                pIndex += 1
                sRecord, pRecord = sIndex, pIndex
            elif s[sIndex] == p[pIndex] or p[pIndex] == '?':
                sIndex += 1
                pIndex += 1
            elif sRecord != -1 and sRecord + 1 < sRight:
                sRecord += 1
                sIndex, pIndex = sRecord, pRecord
            else:
                return False
        return all(p[i] == '*' for i in range(pIndex, pRight))

    def isMatch3(self, s: str, p: str) -> bool:  # ac自动机
        pass

if __name__ == '__main__':
    ss = Solution()
    s = "aa"
    p = "a"
    print('1', ss.isMatch(s, p))
    print('2', ss.isMatch2(s, p))
    s = "aa"
    p = "*"
    print('1', ss.isMatch(s, p))
    print('2', ss.isMatch2(s, p))
    s = "cb"
    p = "?a"
    print('1', ss.isMatch(s, p))
    print('2', ss.isMatch2(s, p))
    s = "adceb"
    p = "*a*b"
    a = [
        [True, True, False, False, False],
        [False, True, True, True, False],
        [False, True, False, True, False],
        [False, True, False, True, False],
        [False, True, False, True, False],
        [False, True, False, True, True]]
    print('1', ss.isMatch(s, p))
    print('2', ss.isMatch2(s, p))
    s = "acdcb"
    p = "a*c?b"
    print('1', ss.isMatch(s, p))
    print('2', ss.isMatch2(s, p))
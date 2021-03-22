'''
32. 最长有效括号
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0

提示：

0 <= s.length <= 3 * 104
s[i] 为 '(' 或 ')'

'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp[i] #最长有效括号
if __name__ =='__main__':
    ss = Solution()
    s = "(()"
    print('1',ss.longestValidParentheses(s))
    s = ")()())"
    print('1',ss.longestValidParentheses(s))
    s = ""
    print('1',ss.longestValidParentheses(s))

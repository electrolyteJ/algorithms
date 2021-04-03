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
    def longestValidParentheses(self, s: str) -> int:  # dp
        # dp[i] 以i下标的最长有效括号子串的长度
        n = len(s)
        dp = [0]*(n)
        max_len = 0
        # 时间复杂度O(n) 空间复杂度O(n)
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i-2 >= 0 else 0) + 2
                elif i - dp[i-1]-1 >= 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if i -
                                       dp[i-1]-2 >= 0 else 0)+2
                max_len = max(max_len, dp[i])
        return max_len

    def longestValidParentheses2(self, s: str) -> int:  # stack
        max_len = 0
        stack = [-1]
        n = len(s)
        # 时间复杂度O(n) 空间复杂度O(n)
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # 栈底始终未最后一个没能被匹配的右括号下标
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len

    def longestValidParentheses3(self, s: str) -> int:
        left=right=max_len = 0
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, 2*right)
            elif right > left:
                left = right = 0
        left = right = 0
        for i in range(n-1,-1,-1):
            if s[i]=='(':
                left+=1
            else:
                right +=1
            if left == right:
                max_len = max(max_len,2*left)
            elif left> right:
                left=right=0
        return max_len
                

if __name__ == '__main__':
    ss = Solution()
    s = "(()"
    print('1', ss.longestValidParentheses(s))
    print('2', ss.longestValidParentheses2(s))
    print('3', ss.longestValidParentheses3(s))
    s = ")()())"
    print('1', ss.longestValidParentheses(s))
    print('2', ss.longestValidParentheses2(s))
    print('3', ss.longestValidParentheses3(s))
    s = ""
    print('1', ss.longestValidParentheses(s))
    print('2', ss.longestValidParentheses2(s))
    print('3', ss.longestValidParentheses3(s))
    s = ")(((((()())()()))()(()))("
    print('1', ss.longestValidParentheses(s))
    print('2', ss.longestValidParentheses2(s))
    print('3', ss.longestValidParentheses3(s))

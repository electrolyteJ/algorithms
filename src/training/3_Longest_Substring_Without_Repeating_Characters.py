'''
3. 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        dp = ['' for _ in range(len(s))]
        dp[0] = s[0]
        for i in range(1, len(s)):
            if s[i] not in dp[i - 1]:
                dp[i] = dp[i - 1] + s[i]
        ret = max(dp, key=len)
        print(dp,ret)
        return len(ret)


if __name__ == '__main__':
    s1 = Solution()
    s = "abcabcbb"
    print('1', s1.lengthOfLongestSubstring(s))
    s = "bbbbb"
    print('1', s1.lengthOfLongestSubstring(s))
    s = "pwwkew"
    print('1', s1.lengthOfLongestSubstring(s))
    s = ""
    print('1', s1.lengthOfLongestSubstring(s))
    s = "aab"
    print('1', s1.lengthOfLongestSubstring(s))  #2

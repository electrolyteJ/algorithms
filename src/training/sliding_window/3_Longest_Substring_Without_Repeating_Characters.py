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
        #时间复杂度O(n) 空间复杂度O(n)
        if not s: return 0
        cur_len,max_len = 0,0
        lookup = []
        for i in range(len(s)):
            while s[i] in lookup:
                lookup.pop(0)
                cur_len -=1
            cur_len +=1
            lookup.append(s[i])
            max_len = max(max_len,cur_len)
        return max_len

    def lengthOfLongestSubstring1(self, s: str) -> int:
        if not s:return 0
        #滑动窗口模板
        import collections
        left,right=0,0
        counter,max_len=0,0
        lookup = collections.defaultdict(int)
        while right < len(s):
            if lookup[s[right]] > 0 :
                counter +=1
            lookup[s[right]] +=1
            right +=1
            while counter > 0:
                if lookup[s[left]] > 1:
                    counter -=1
                lookup[s[left]] -=1
                left +=1
            max_len = max(max_len,right - left)
        return max_len

if __name__ == '__main__':
    s1 = Solution()
    s = "abcabcbb"
    print('1', s1.lengthOfLongestSubstring(s))
    print('1', s1.lengthOfLongestSubstring1(s))
    s = "bbbbb"
    print('1', s1.lengthOfLongestSubstring(s))
    s = "pwwkew"
    print('1', s1.lengthOfLongestSubstring(s))
    s = ""
    print('1', s1.lengthOfLongestSubstring(s))
    s = "aab"
    print('1', s1.lengthOfLongestSubstring(s))  #2

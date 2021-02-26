'''
76. 最小覆盖子串
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"
 

提示：

1 <= s.length, t.length <= 105
s 和 t 由英文字母组成
 

进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？
通过次数111,206提交次数272,905

'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t :return 0
        import collections
        left,right=0,0
        min_len,counter =float('inf'),len(t)
        lookup = collections.defaultdict(int)
        ret =[]
        #时间复杂度O(s+t)
        for t1 in t:
            lookup[t1] +=1
        while right < len(s):
            if lookup[s[right]] > 0:
                counter -=1
            lookup[s[right]] -=1
            right +=1
            while counter == 0:
                if min_len > right-left:
                    min_len = right-left
                    ret = s[left:right]
                if lookup[s[left]] == 0:
                    counter +=1
               
                lookup[s[left]] +=1
                left +=1
        return ret
                




if __name__ == '__main__':
    s1 = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print('1',s1.minWindow(s,t))
    s = "a"
    t = "a"
    print('1',s1.minWindow(s,t))
'''
727. 最小窗口子序列（滑动窗口）

给定字符串 S and T，找出 S 中最短的（连续）子串 W ，使得 T 是 W 的 子序列 。

如果 S 中没有窗口可以包含 T 中的所有字符，返回空字符串 “”。
如果有不止一个最短长度的窗口，返回开始位置最靠左的那个。

示例 1：
输入：
S = "abcdebdde", T = "bde"
输出："bcde"
解释：
"bcde" 是答案，因为它在相同长度的字符串 "bdde" 出现之前。
"deb" 不是一个更短的答案，因为在窗口中必须按顺序出现 T 中的元素。
 
注：
所有输入的字符串都只包含小写字母。
S 长度的范围为 [1, 20000]。
T 长度的范围为 [1, 100]。
'''
class Solution:
    def minWindow(self,s, t):#（滑动窗口）
        left,right =0,0
        min_len,counter=float('inf'),len(t)
        ret =''
        import collections
        lookup = collections.defaultdict(int)
        for e in t:
            lookup[e] += 1
        #O(n*n)
        while right < len(s):
            if lookup[s[right]] >0:
                counter -=1
            # lookup[s[right]] -= 1
            right +=1
            tmp = left
            t_i = 0
            while counter == 0:
                if s[left] == t[t_i]:
                    if t_i ==0:
                        tmp = left
                    t_i +=1
                # lookup[s[left]] +=1
                left +=1
                if left > right:
                    counter = -1
                elif t_i == len(t):
                    counter = -2
            if counter == -2 and right - tmp < min_len:
                min_len = right - tmp
                ret = s[tmp:right]
            elif counter ==-1:
                counter = len(t)
        return ret

if __name__=='__main__':
    s1 = Solution()
    s ='abcdebdde'
    t ='bde'
    print('1',s1.minWindow(s,t))
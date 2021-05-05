'''
557. 反转字符串中的单词 III
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
示例：
输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"
提示：
在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        aa = s.split(' ')
        s = ''
        for a in aa:
            s +=''.join(reversed(a))+' '
        return s.strip()
    def reverseWords2(self, s: str) -> str:
        ret=''
        stack=[]
        for i in range(len(s)):
            if s[i].isspace():
                while stack:
                    ret +=stack.pop()
                ret+=s[i]
                continue
            stack.append(s[i])
        while stack:
            ret += stack.pop()
        return ret
    def reverseWords3(self, s: str) -> str:
        ret = ''
        left, right = 0, 0
        n = len(s)
        while right < n:
            while right < n and not s[right].isspace():
                right+=1
            for i in range(right-1,left-1,-1):
                ret +=s[i]
            while right < n and s[right].isspace():
                right+=1
                ret+=' '
            left = right
        return ret


if __name__ =='__main__':
    ss = Solution()
    s = "Let's take LeetCode contest"
    print('1',ss.reverseWords(s))
    print('2',ss.reverseWords2(s))
    print('3',ss.reverseWords3(s))

'''
151. 翻转字符串里的单词
给定一个字符串，逐个翻转字符串中的每个单词。
说明：
无空格字符构成一个 单词 。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
示例 1：
输入："the sky is blue"
输出："blue is sky the"
示例 2：
输入："  hello world!  "
输出："world! hello"
解释：输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入："a good   example"
输出："example good a"
解释：如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
示例 4：

输入：s = "  Bob    Loves  Alice   "
输出："Alice Loves Bob"
示例 5：
输入：s = "Alice does not even like bob"
输出："bob like even not does Alice"
提示：
1 <= s.length <= 104
s 包含英文大小写字母、数字和空格 ' '
s 中 至少存在一个 单词
进阶：请尝试使用 O(1) 额外空间复杂度的原地解法。
'''


class Solution:
    def reverseWords1(self, s: str) -> str:
        # 时间复杂度O(n) 空间复杂度O(n)
        return ' '.join(reversed(s.split()))

    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1

        # 去掉字符串末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1

        # 将字符串间多余的空白字符去除
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1

        return output

    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            # 循环至单词的末尾
            while end < n and l[end] != ' ':
                end += 1
            # 翻转单词
            self.reverse(l, start, end - 1)
            # 更新start，去找下一个单词
            start = end + 1
            end += 1

    def reverseWords2(self, s: str) -> str:
        l = self.trim_spaces(s)

        # 翻转字符串
        self.reverse(l, 0, len(l) - 1)

        # 翻转每个单词
        self.reverse_each_word(l)

        return ''.join(l)

    def reverseWords3(self, s: str) -> str:#双端队列
        left, right = 0, len(s)-1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1
        import collections
        #时间复杂度O(n) 空间复杂度O(n)
        q, word = collections.deque(), []
        while left <= right:
            if s[left] == ' ' and word:
                q.appendleft(''.join(word))  # 头部插入
                word.clear()
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        q.appendleft(''.join(word))
        return ' '.join(q)


if __name__ == '__main__':
    ss = Solution()
    s = "the sky is blue"
    print('1', ss.reverseWords1(s))
    print('2', ss.reverseWords2(s))
    print('3', ss.reverseWords3(s))
    s = "  hello world!  "
    print('1', ss.reverseWords1(s))
    print('2', ss.reverseWords2(s))
    print('3', ss.reverseWords3(s))
    s = "a good   example"
    print('1', ss.reverseWords1(s))
    print('2', ss.reverseWords2(s))
    print('3', ss.reverseWords3(s))
    s = "  Bob    Loves  Alice   "
    print('1', ss.reverseWords1(s))
    print('2', ss.reverseWords2(s))
    print('3', ss.reverseWords3(s))
    s = "Alice does not even like bob"
    print('1', ss.reverseWords1(s))
    print('2', ss.reverseWords2(s))
    print('3', ss.reverseWords3(s))

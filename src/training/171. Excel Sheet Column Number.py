'''
171. Excel表列序号
给定一个Excel表格中的列名称，返回其相应的列序号。
例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701
'''
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # ret=0
        # for c in columnTitle:
        #     ret = ret*26+ ord(c)-ord('A')+1
        # return  ret
        import functools
        return functools.reduce(lambda x, y: x*26+y, [ord(c)-ord('A')+1 for c in columnTitle])
if __name__ =='__main__':
    s = Solution()
    columnTitle = "A"
    print('1',s.titleToNumber(columnTitle))
    columnTitle = "AB"
    print('1',s.titleToNumber(columnTitle))
    columnTitle = "ZY"
    print('1',s.titleToNumber(columnTitle))

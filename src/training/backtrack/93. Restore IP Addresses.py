'''
93. 复原 IP 地址
给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。

有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。

示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：

输入：s = "0000"
输出：["0.0.0.0"]
示例 3：

输入：s = "1111"
输出：["1.1.1.1"]
示例 4：

输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
示例 5：

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

提示：

0 <= s.length <= 3000
s 仅由数字组成
'''


class Solution:
    def restoreIpAddresses(self, s: str):
        def backtrace(pos):
            if pos >= len(s):
                print(visited)
                if len(visited)==4:
                    ret.append('.'.join(visited))
                return
            for i in range(pos, len(s)):
                l = i+1-pos
                if len(visited) >= 4 or l > 1 and int(s[pos]) == 0:
                    break
                if 0 > int(s[pos:i+1]) or int(s[pos:i+1]) > 255:
                    break
                visited.append(s[pos:i+1])
                backtrace(i+1)
                visited.pop()

        ret = []
        visited=[]
        backtrace(0)
        return ret

if __name__ =='__main__':
    ss = Solution()
    s = "25525511135"
    print('1',ss.restoreIpAddresses(s))
    s = "0000"
    print('1',ss.restoreIpAddresses(s))
    s = "1111"
    print('1',ss.restoreIpAddresses(s))
    s = "010010"
    print('1',ss.restoreIpAddresses(s))
    s = "101023"
    print('1',ss.restoreIpAddresses(s))

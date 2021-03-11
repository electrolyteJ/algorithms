'''
739. 每日温度
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
'''
class Solution:
    def dailyTemperatures1(self, T):
        #时间复杂度O(mn) 空间复杂度O(m)
        n = len(T)
        ans, nxt, big = [0] * n, dict(), 10**9
        for i in range(n - 1, -1, -1):
            warmer_index = min(nxt.get(t, big) for t in range(T[i] + 1, 102))
            if warmer_index != big:
                ans[i] = warmer_index - i
            nxt[T[i]] = i
        return ans
    def dailyTemperatures2(self, T):
        #时间复杂度O(n) 空间复杂度O(n)
        length = len(T)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = T[i]
            while stack and temperature > T[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans

if __name__ == '__main__':
    s = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print('1', s.dailyTemperatures1(temperatures))
    print('2', s.dailyTemperatures2(temperatures))

'''
767. 重构字符串
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。

若可行，输出任意可行的结果。若不可行，返回空字符串。

示例 1:

输入: S = "aab"
输出: "aba"
示例 2:

输入: S = "aaab"
输出: ""
注意:

S 只包含小写字母并且长度在[1, 500]区间内。
'''


class Solution:
    def reorganizeString(self, S: str) -> str:
        #时间复杂度O(n logalphabet) 空间复杂度O(alphabet)
        if len(S)<2:
            return S
        n = len(S)
        import collections,heapq
        counter = collections.Counter(S)
        q = [(-v,k) for k,v in counter.items()]
        heapq.heapify(q)
        if -q[0][0]>(n+1)//2:
            return ""
        ans=[]
        while len(q)>1:
            _,letter1 = heapq.heappop(q)
            _,letter2 = heapq.heappop(q)
            ans.extend([letter1,letter2])
            counter[letter1] -=1
            counter[letter2] -=1
            if counter[letter1]>0:
                heapq.heappush(q,(-counter[letter1],letter1))
            if counter[letter2] >0:
                heapq.heappush(q,(-counter[letter2],letter2))
            
        if q:
            ans.append(q[0][1])
        return ''.join(ans)


    def reorganizeString2(self, S: str) -> str:
        if not len(S):
            return S
        import collections 
        counter = collections.Counter(S)
        max_c=max(counter.items(),key=lambda x:x[1])[1]
        n=len(S)
        if max_c> (n+1)//2:
            return ""
        ret = ['']*n
        even,odd = 0, 1
        for k,v in counter.items():
            while v > 0 and odd < n and v <= n//2:
                ret[odd] = k
                odd +=2
                v -=1
            while v > 0 and even < n:
                ret[even] = k
                even += 2
                v -= 1
        return ''.join(ret)
        

if __name__ == '__main__':
    s =Solution()
    S = "aab"
    print('1',s.reorganizeString(S))
    print('2',s.reorganizeString2(S))
    S = "aaab"
    print('1',s.reorganizeString(S))
    print('2',s.reorganizeString2(S))
    S = "baaba"
    print('1',s.reorganizeString(S))
    print('2',s.reorganizeString2(S))

'''
692. 前K个高频单词
给一非空的单词列表，返回前 k 个出现次数最多的单词。
返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。
示例 1：
输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。
示例 2：
输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。
注意：
假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。
输入的单词均由小写字母组成。
扩展练习：
尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决。
'''
from typing import List
import functools
class Solution:
    def topKFrequent1(self, words: List[str], k: int) -> List[str]:#hash+快排
        import collections
        import functools
        #时间复杂度O(l*n)
        counter = collections.Counter(words)  # 空间复杂度O(l*m)
        ret = list(counter.keys())  # 空间复杂度O(l*m)
        #时间复杂度O(l*mlogm)
        def sort_rule(cur, pre):
            #按照单词出现的次数从大到小
            if counter[cur] > counter[pre]:
                return -1
            elif counter[cur] < counter[pre]:
                return 1
            else:  # 如果出现次数想通则按照字符排序
                if cur > pre:  # b > a 返回1则b排在后面；返回-1则b排在前面
                    return 1
                elif cur < pre:
                    return -1
                else:
                    return 0
        ret.sort(key=functools.cmp_to_key(sort_rule))
        #最后时间复杂度O( (l*n)+l*mlogm) 空间复杂度O(l*m)
        return ret[:k]
    def topKFrequent2(self, words: List[str], k: int) -> List[str]:  # 优先队列
        import collections,heapq
        #时间复杂度O(l*n)
        counter = collections.Counter(words)  # 空间复杂度O(l*m)
        q = []
        #时间复杂度O(l*mlongk) 空间复杂度O(l*k)
        for word,cnt in counter.items():#无序遍历
            heapq.heappush(q,(E(word,cnt)) )
            if len(q)>k:
                heapq.heappop(q)
        ret = []
        while q:
            ret.append(heapq.heappop(q).word)
        #时间复杂度O(l*n+l*mlongk) 空间复杂度O(l*(m+k))
        return ret[::-1]
class E:  # 堆顶的元素为次数最少 and 字母排序最靠后
    def __init__(self, word, cnt):
        self.word = word
        self.cnt = cnt

    def __lt__(self, other):
        if self.cnt != other.cnt:
            return self.cnt < other.cnt
        return self.word > other.word
    def __repr__(self):
        return '%s:%s' % (self.word, self.cnt)

if __name__ =='__main__':
    s = Solution()
    words = ["i", "love", "leetcode", "i", "love", "coding"]; k = 2
    k = 2
    print('1',s.topKFrequent1(words, k))
    print('2',s.topKFrequent2(words, k))
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]; k = 4
    print('1',s.topKFrequent1(words, k))
    print('2',s.topKFrequent2(words, k))

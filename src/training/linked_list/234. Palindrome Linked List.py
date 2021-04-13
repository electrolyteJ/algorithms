'''
234. 回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''

from src.common.list import create_listnode,ListNode
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:return True
        def reverse(h):
            ret = None
            cur = h
            while cur:
                cur.next,cur,ret = ret,cur.next,cur
            return ret
        frist_of_end,fast=head,head
        while fast.next and fast.next.next:
            frist_of_end,fast=frist_of_end.next,fast.next.next
        frist,sec = head,reverse(frist_of_end.next)
        while sec:
            if frist.value !=sec.value:
                return False
            frist,sec=frist.next,sec.next
        return True

if __name__ == '__main__':
    s = Solution()
    head = create_listnode([1,2,])
    print(s.isPalindrome(head))
    head = create_listnode([1,2,2,1])
    print(s.isPalindrome(head))

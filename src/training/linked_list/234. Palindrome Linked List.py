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
            cur = h
            ret = None
            while cur:
                cur.next, cur, ret = ret, cur.next, cur
            return ret
        def end_of_first_half(h):
            slow,fast=h,h
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        first =  head
        first_half_end = end_of_first_half(head)
        second = reverse(first_half_end.next)
        print(first,second)
        ret =True
        while ret and second:
            if first.value != second.value:
                ret = False
            first = first.next
            second = second.next
        first_half_end.next = reverse(second)
        return ret





if __name__ == '__main__':
    s = Solution()
    head = create_listnode([1,2,])
    print(s.isPalindrome(head))
    head = create_listnode([1,2,2,1])
    print(s.isPalindrome(head))

# -*- coding: UTF-8 -*-
"""
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例 1：


输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]
 

提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
"""

from common.list import ListNode, create_listnode


class Solution:
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(-1)
        l = dummy_head
        #时间复杂度O(n+m) 空间复杂度O(1)
        while l1 and l2:
            if l1.value <= l2.value:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            l = l.next
        l.next =  l2 if l2 else l1
        return dummy_head.next

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:#递归
         #时间复杂度O(n+m) 空间复杂度O(n+m)
        if not l1:
             return l2
        elif not l2:
            return l1
        elif l1.value <= l2.value:
            l1.next = self.mergeTwoLists2(l1.next,l2)
            return l1
        elif l2.value < l1.value:
            l2.next = self.mergeTwoLists2(l1,l2.next)
            return l2

if __name__ == '__main__':
    s = Solution()
    print(
        '1',
        s.mergeTwoLists1(create_listnode([1, 2, 4]), create_listnode([1, 3,
                                                                     4])))
    print(
        '2',
        s.mergeTwoLists2(create_listnode([1, 2, 4]), create_listnode([1, 3,
                                                                     4])))
    print('1', s.mergeTwoLists1(create_listnode([]), create_listnode([])))
    print('2', s.mergeTwoLists2(create_listnode([]), create_listnode([])))
    print('1', s.mergeTwoLists1(create_listnode([]), create_listnode([0])))
    print('2', s.mergeTwoLists2(create_listnode([]), create_listnode([0])))

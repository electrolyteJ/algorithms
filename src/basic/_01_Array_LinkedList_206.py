'''
206. 反转链表
难度：简单
反转一个单链表。

示例:

输入: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
输出: 5 -> 4 -> 3 -> 2 -> 1 -> NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

'''

from mock.ListNode import ListNode


class Solution:  # linked list :1->2->3->4->5->None
    def reverseList0(self, head: ListNode) -> ListNode:  # 迭代
        cur_node, ret_node = head, None
        while cur_node:
            tmp = cur_node.next
            cur_node.next = ret_node
            ret_node = cur_node
            cur_node = tmp
        return ret_node

    def reverseList1(self, head: ListNode) -> ListNode:  # 递归
        if not head or not head.next:
            return head
        p = self.reverseList1(head.next)
        head.next.next = head
        head.next = None
        return p


def main():
    datas = [1, 2, 3, 4, 5]
    listnode = ListNode.create(datas)
    print('raw datas: {}'.format(listnode))
    s = Solution()
    print('迭代:{}'.format(s.reverseList0(listnode)))
    listnode2 = ListNode.create(datas)
    print('递归:{}'.format(s.reverseList1(listnode2)))


if __name__ == '__main__':
    main()

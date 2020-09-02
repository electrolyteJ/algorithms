'''
24. 两两交换链表中的节点
难度：中等
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:

给定 1->2->3->4->5, 你应该返回 2->1->4->3->5.
'''

from mock.ListNode import ListNode


class Solution:
    def swapPairs0(self, head: ListNode) -> ListNode:  # 迭代
        if not head or not head.next:
            return head
        first = head
        sec = head.next
        while sec:
            sec.next, first.next, = first, sec.next
            if sec.next:
                first = sec.next
            # if sec.next.next:
            #     sec = sec.next.next
            print(first, sec)
            break

            # if sec.next:
            #     sec = sec.next.next
        return sec

    def swapPairs1(self, head: ListNode) -> ListNode:  # 递归
        pass


def main():
    datas = [1, 2, 3, 4, 5]
    listnode = ListNode.create(datas)
    print('raw datas--->{}'.format(listnode))
    s = Solution()
    print('迭代--->{}'.format(s.swapPairs0(listnode)))
    listnode2 = ListNode.create(datas)
    print('递归--->{}'.format(s.swapPairs1(listnode2)))


if __name__ == '__main__':
    main()

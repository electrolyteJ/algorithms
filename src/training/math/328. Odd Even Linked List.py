'''
328. 奇偶链表
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:

输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:

输入: 2->1->3->5->6->4->7->NULL 
输出: 2->3->6->7->1->5->4->NULL
说明:

应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
'''
from src.common.list import ListNode,create_listnode
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:return head
        even_head=head.next
        odd,even=head,even_head
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head
if __name__ =='__main__':
    s = Solution()
    head = create_listnode([1, 2, 3, 4, 5])
    print('1', s.oddEvenList(head))
    head = create_listnode([2, 1, 3,5, 6, 4,7])
    print('1', s.oddEvenList(head))

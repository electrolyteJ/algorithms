'''
445. 两数相加 II
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。
进阶：如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7
'''
from common.list import create_listnode, ListNode
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1=[]
        stack2=[]
        while l1:
            stack1.append(l1.value)
            l1=l1.next
        while l2:
            stack2.append(l2.value)
            l2 = l2.next
        #时间复杂度O(max(m,n)) 空间复杂度O(n+m)
        ret=None
        add=0
        while stack1 or stack2 or add !=0:
            x = stack1.pop() if stack1 else 0
            y =stack2.pop() if stack2 else 0
            sum_ret = x+y+add
            add =sum_ret//10
            node =ListNode(sum_ret%10)
            node.next ,ret=ret,node
        return ret
if __name__=='__main__':
    s = Solution()
    l1= create_listnode([7,2,4,3])
    l2 = create_listnode([5,6,4])
    print('1',s.addTwoNumbers(l1,l2))

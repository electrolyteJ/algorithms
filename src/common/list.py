'''
  Linkedlist
  - Singly linked list
  - Doubly linked list
  - Multiply linked list
  - Circular linked list
  - Hash linking
'''
from typing import Union, List

class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x, random_index=None, is_random_list=False):
        self.value = x
        self.next = None
        self.random = None
        self.random_index = random_index
        self.is_random_list = is_random_list

    def __repr__(self): 
        return 'Node({})'.format(self.value)
    def __str__(self):
        if self and self.is_random_list:
            return self.joinStr(self.next, "[{},{}]".format(self.value,self.random_index))
        elif self:
            return self.joinStr(self.next, "{}".format(self.value))

    def joinStr(self, node, formatStr):
        if node and self.is_random_list:
            return self.joinStr(node.next, formatStr+ str("->[{},{}]".format(node.value, node.random_index)))
        elif node:
            return self.joinStr(node.next, formatStr + str("->{}".format(node.value)))
        else:
            return str(formatStr+str('->None'))


def create_listnode(data):
    size=len(data)
    listNodes=[None]*size
    for i in range(size):
        node=ListNode(data[i])
        listNodes[i]=node
        if i != 0:
            listNodes[i-1].next=node
    return listNodes[0] if len(listNodes) > 0 else None


def create_listnode_with_random(data:List[List[int]]):
    size=len(data)
    listNodes=[None]*size
    for i in range(size):
        node=ListNode(data[i][0],data[i][1],True)
        listNodes[i]=node
        if i != 0:
            listNodes[i-1].next=node
    for i in range(size):
        if data[i][1]:
            listNodes[i].random=listNodes[data[i][1]]
    return listNodes[0] if len(listNodes) > 0 else None


if __name__ == '__main__':

    datas=[1, 2, 3, 4, 5]
    listNode=create_listnode(datas)
    print('{}'.format(listNode))
    head = create_listnode_with_random(
        [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    print(head)
    while head:
        print(head.random_index, head.random.value if head.random else None)
        head =head.next


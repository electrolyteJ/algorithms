'''
  Linkedlist
  - Singly linked list
  - Doubly linked list
  - Multiply linked list
  - Circular linked list
  - Hash linking
'''

class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.value = x
        self.next = None

    def __str__(self):
        return self.joinStr(self, "{}".format(self.value))

    def joinStr(self, node, formatStr):
        if node.next:
            return self.joinStr(node.next, formatStr +
                                str("->{}".format(node.next.value)))
        else:
            return str(formatStr+str('->None'))


def create_listnode(data):
    size = len(data)
    listNodes = [None]*size
    for i in range(size):
        node = ListNode(data[i])
        listNodes[i] = node
        if i != 0:
            listNodes[i-1].next = node
    return listNodes[0] if len(listNodes) > 0 else None


if __name__ == '__main__':

    datas = [1, 2, 3, 4, 5]
    listNode = create_listnode(datas)
    print('{}'.format(listNode))

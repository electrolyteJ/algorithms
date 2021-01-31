import heapq


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.value = x
        self.next = None

    def __str__(self):
        # return self.joinStr(self, "linked list :{}".format(self.value))
        return self.joinStr(self, "{}".format(self.value))

    def joinStr(self, node, formatStr):
        if node.next:
            return self.joinStr(node.next, formatStr +
                                str("->{}".format(node.next.value)))
        else:
            return str(formatStr+str('->None'))
            # return str(formatStr)

    @staticmethod
    def create(data):
        size = len(data)
        listNodes = [None]*size
        for i in range(size):
            node = ListNode(data[i])
            listNodes[i] = node
            if i != 0:
                listNodes[i-1].next = node
        # for i in range(len(listNodes)):
            # print("create:index==>{} node==>value:{},next value:{}".format(
                # i, listNodes[i].value, listNodes[i].next.value if listNodes[i].next else None))
        return listNodes[0] if len(listNodes) > 0 else None


class MaxHeap():
    def __init__(self, nums):
        self.rev_nums = [-e for e in nums]
        heapq.heapify(self.rev_nums)

    def offer(self, e):
        heapq.heappush(self.rev_nums, -e)

    def poll(self):
        return -heapq.heappop(self.rev_nums)

    def peek(self):
        return -self.rev_nums[0]


class TreeNode:
    def __init__(self, v):
        self.v = v
        self.left, self.right = None, None


if __name__ == '__main__':
    # O(log n)
    h = MaxHeap([1, 3, 4, 5, 5, 2, 4])
    print(h.peek())
    h.offer(7)
    print(h.poll())
    h.offer(6)
    print(h.poll())
    datas = [1, 2, 3, 4, 5]
    listNode = ListNode.create(datas)
    print('{}'.format(listNode))

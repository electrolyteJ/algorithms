
import asyncio


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.value = x
        self.next = None

    def __str__(self):
        return self.joinStr(self, "linked list :{}".format(self.value))

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


def main():
    datas = [1, 2, 3, 4, 5]
    listNode = ListNode.create(datas)
    print('{}'.format(listNode))


async def async_send0():
    await asyncio.sleep(1)
    print("async_send0")


async def await0():
    print("await0")


async def await1():
    print("await1")
    await await11()
    await await12()
    await await13()


async def await11():
    print("await11")


async def await12():
    print("await12")


async def await13():
    print("await13")


async def await2():
    print("await2")


async def async_send1():
    # await async_send0()
    await await0()
    await await1()
    await asyncio.sleep(4)
    await await2()
    print("async_send1")


def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        print("res {}".join(e.value))
        return e.value


if __name__ == '__main__':
    main()
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(asyncio.wait(
        [async_send0(), async_send1()]
    ))
    loop.close()

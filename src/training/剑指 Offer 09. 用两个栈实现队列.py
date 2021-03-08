'''
剑指 Offer 09. 用两个栈实现队列
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
'''

class CQueue:

    def __init__(self):
        self.in_stack=[]
        self.out_stack=[]

    def appendTail(self, value: int) -> None:
        self.in_stack.append(value)

    def deleteHead(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                v = self.in_stack.pop()
                self.out_stack.append(v)
        return self.out_stack.pop() if self.out_stack else -1


if __name__ =='__main__':
    c = CQueue()
    print('appendTail',c.appendTail(3))
    print('appendTail',c.appendTail(5))
    print('deleteHead',c.deleteHead())
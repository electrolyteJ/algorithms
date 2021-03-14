'''
225. 用队列实现栈
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。

提示：

1 <= x <= 9
最多调用100 次 push、pop、top 和 empty
每次调用 pop 和 top 都保证栈不为空
 

进阶：你能否实现每种操作的均摊时间复杂度为 O(1) 的栈？换句话说，执行 n 个操作的总时间复杂度 O(n) ，尽管其中某个操作可能需要比其他操作更长的时间。你可以使用两个以上的队列。
'''


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.q1 = collections.deque()
        self.q2 = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1,self.q2=self.q2,self.q1


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q1.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q1


def main():
    s = MyStack()
    s.push(1)
    s.push(2)
    print(s.top())
    print(s.pop())
    print(s.pop())
    print(s.empty())


if __name__ == '__main__':
    main()

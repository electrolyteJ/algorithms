'''
102. 二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
'''


from mock.tree import create_treenode
from queue import Queue


class Solution:
    def levelOrder1(self, root):  # bfs
        if not root:
            return []
        q, ret = Queue(), []
        q.put(root)
        #visited =set(root)
        while q.qsize() > 0:
            current_level = []
            for _ in range(0, q.qsize()):
                node = q.get()
                current_level.append(node.value)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            ret.append(current_level)
        return ret

    def dfs(self,node, level):
        if not node:return
        if len(self.ret) <level+1:
            self.ret.append([])
        self.ret[level].append(node.value)

        self.dfs(node.left,level+1)
        self.dfs(node.right,level+1)
    def levelOrder2(self, root):  # dfs
        
        if not root :return[]
        self.ret = []
        self.dfs(root,0)
        return   self.ret


if __name__ == "__main__":
    s = Solution()
    l = [3, 9, 20, None, None, 15, 7]
    t = create_treenode(l)
    print(t)
    print('1', s.levelOrder1(t))
    print('2', s.levelOrder2(t))

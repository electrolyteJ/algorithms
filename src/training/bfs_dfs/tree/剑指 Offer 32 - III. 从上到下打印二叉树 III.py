'''
剑指 Offer 32 - III. 从上到下打印二叉树 III
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]
 

提示：

节点总数 <= 1000
'''


class Solution:
    def levelOrder(self, root):
        if not root:return []
        import collections
        q  = collections.deque([root])
        ret=[]
        level=1
        while q:
            current_level = collections.deque()
            for _ in range(len(q)):
                node = q.popleft()
                if level &1:
                    current_level.append(node.value)
                else:
                    current_level.appendleft(node.value)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
            ret.append(list(current_level))
        return ret
                
        
if __name__ == '__main__':
    s = Solution()
    from src.common.tree import create_treenode
    root = create_treenode([3, 9, 20, None, None, 15, 7])
    print(root)
    print('1', s.levelOrder(root))

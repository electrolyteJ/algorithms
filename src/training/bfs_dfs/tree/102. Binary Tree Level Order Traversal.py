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
]
'''
from src.common.tree import create_treenode
class Solution:
    def levelOrder(self, root):#bfs
        if not root:return []
        import collections
        q = collections.deque([root])
        ret = []
        while q:
          current_level = []
          for _ in range(len(q)):
            node = q.popleft()
            current_level.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
          ret.append(current_level)
        return ret

    def levelOrder2(self, root):  # dfs
        if not root:return []
        def dfs(node,level):
          if not node:return 
          if level > len(ret):
            ret.append([])
          ret[level-1].append(node.value)
          dfs(node.left,level+1)
          dfs(node.right,level+1)
        ret = []
        dfs(root,1)
        return ret
            
if __name__ =='__main__':
    s = Solution()
    root = create_treenode([3, 9, 20, None, None, 15, 7])
    print(root)
    print('1',s.levelOrder(root))
    print('2', s.levelOrder2(root))

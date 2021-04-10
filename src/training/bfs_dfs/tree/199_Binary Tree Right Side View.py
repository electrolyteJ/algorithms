'''
199. 二叉树的右视图
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''
from src.common.tree import create_treenode
class Solution:
    def rightSideView_bfs(self, root):
        if not root:return []
        #bfs 时间复杂度O(n) 空间复杂度O(n)
        ret = []
        import collections
        q = collections.deque([root])
        while q:
            ret.append(q[-1].val)
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ret


    def rightSideView_dfs(self, root):
        if not root:return []
        stack,ret =[(root,0)],dict()
        max_depth =0
        while stack:
            node,depth = stack.pop()
            if node:
                # ret.append(node.value)
                max_depth = max(max_depth,depth)
                ret.setdefault(depth, node.value)
                stack.append((node.left,depth+1))
                stack.append((node.right,depth+1))
        return [ret[d] for d in range(max_depth+1)]

if __name__ == '__main__':
    s = Solution()
    root = create_treenode([1, 2, 3, None, 5, None, 4])
    print('bfs', s.rightSideView_bfs(root))
    print('dfs', s.rightSideView_dfs(root))
    # print('pre-order', root.preorder)
    root = create_treenode([1, 2])
    print(root)
    print('bfs', s.rightSideView_bfs(root))
    print('dfs', s.rightSideView_dfs(root))

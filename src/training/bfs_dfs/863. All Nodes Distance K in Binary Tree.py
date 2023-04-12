'''
863. 二叉树中所有距离为 K 的结点
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。

示例 1：

输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
输出：[7,4,1]
解释：
所求结点为与目标结点（值为 5）距离为 2 的结点，
值分别为 7，4，以及 1

注意，输入的 "root" 和 "target" 实际上是树上的结点。
上面的输入仅仅是对这些对象进行了序列化描述。

提示：

给定的树是非空的。
树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
目标结点 target 是树上的结点。
0 <= K <= 1000.
'''


class Solution:

    def distanceK(self, root, target, K: int):
        if not root:return []
        #时间复杂度O(n) 空间复杂度O(n)
        def dfs(node, parent):
            if not node:
                return
            node.par = parent
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        import collections
        q = collections.deque([(target, 0)])
        ret = []
        visited = {target}
        while q:
            if q[0][1] == K:
                return [n.val for n, _ in q]
            for _ in range(len(q)):
                node, depth = q.popleft()
                for sub_node in (node.left, node.right, node.par):
                    if sub_node and sub_node not in visited:
                        visited.add(node)
                        q.append((sub_node, depth+1))
        return ret

    def distanceK2(self, root, target, K: int):
        ret = []
        def subtree_add(node,d):
            if not node:
                return
            elif d==K:
                ret.append(node.value)
            else:
                subtree_add(node.left,d+1)
                subtree_add(node.right,d+1)
        def dfs(node):
            if not node:
                return -1
            elif node == target:
                subtree_add(node,0)
                return 1
            else:
                l,r=dfs(node.left),dfs(node.right)
                if l !=-1:
                    if l==K:ret.append(node.value)
                    subtree_add(node.right,l+1)
                    return l+1
                elif r !=-1:
                    if r == K: ret.append(node.value)
                    subtree_add(node.left,r+1)
                    return r+1
                else:
                    return -1
        dfs(root)
        return ret
            
            
if __name__ =='__main__':
    s = Solution()
    from common.tree import create_treenode
    root = create_treenode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    target = root[1]
    K = 2
    print(root,target)
    #[7, 4, 1]
    print('1', s.distanceK(root, target, K))
    print('2', s.distanceK2(root, target, K))

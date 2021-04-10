'''
144. 二叉树的前序遍历
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

示例 1：

输入：root = [1,null,2,3]
输出：[1,2,3]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[1,2]
示例 5：


输入：root = [1,null,2]
输出：[1,2]
 

提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100

'''
from src.common.tree import create_treenode
class Solution:
    def preorderTraversal1(self, root):#递归
        if not root:
            return []
        l = self.preorderTraversal1(root.left)
        r = self.preorderTraversal1(root.right)
        return [root.value] +l+r
        
    def preorderTraversal2(self, root):#迭代
        if not root:
            return []
        stack,ret = [root],[]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.value)
                stack.append(node.right)
                stack.append(node.left)
        return ret
if __name__ =='__main__':
    s = Solution()
    root = create_treenode([1,None,2,None,None,3])
    print(root)
    print('1',s.preorderTraversal1(root))
    print('2',s.preorderTraversal2(root))
    root = create_treenode([1,2,3,4,None,5])
    print('1',s.preorderTraversal1(root))
    print('2',s.preorderTraversal2(root))
    
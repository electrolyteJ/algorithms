'''
105. 从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
'''
from src.common.tree import Node

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root_v = preorder[0]
        root_i = inorder.index(root_v)

        left = inorder[:root_i]
        left_subtree = self.buildTree(preorder[1:1+len(left)], left)
        right_subtree = self.buildTree(
            preorder[1+len(left):], inorder[1+root_i:])

        node = Node(root_v)
        node.left = left_subtree
        node.right = right_subtree

        return node

    def buildTree1(self, preorder, inorder):#递归
        #时间复杂度O(n) 空间复杂度O(n)
        def recur(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            preorder_root_i = preorder_left
            inoder_root_i = index[preorder[preorder_root_i]]
            node = Node(preorder[preorder_root_i])
            left_subtree_len = inoder_root_i - inorder_left
            node.left = recur(preorder_root_i+1, preorder_root_i +
                              left_subtree_len, inorder_left, inoder_root_i-1)
            node.right = recur(preorder_root_i+left_subtree_len+1,
                               preorder_right, inoder_root_i+1, inorder_right)
            return node

        index = {e: i for i, e in enumerate(inorder)}
        return recur(0, len(preorder)-1, 0, len(preorder)-1)

        

    def buildTree2(self, preorder, inorder):  # 迭代
        if not preorder:
            return None
        #时间复杂度O(n) 空间复杂度O(n)
        root = Node(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            if node.value != inorder[inorderIndex]:
                node.left = Node(preorderVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].value == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = Node(preorderVal)
                stack.append(node.right)

        return root

if __name__ =='__main__':
    s = Solution()
    preorder = [3, 9, 20, 15, 7] #[根节点 [左子树] [右子树]]
    inorder = [9, 3, 15, 20, 7]  # [[左子树] 根节点 [右子树]]
    print('1', s.buildTree1(preorder,inorder))
    print('2', s.buildTree2(preorder, inorder))

'''
662. 二叉树最大宽度
给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。

每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。

示例 1:

输入: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

输出: 4
解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
示例 2:

输入: 

          1
         /  
        3    
       / \       
      5   3     

输出: 2
解释: 最大值出现在树的第 3 层，宽度为 2 (5,3)。
示例 3:

输入: 

          1
         / \
        3   2 
       /        
      5      

输出: 2
解释: 最大值出现在树的第 2 层，宽度为 2 (3,2)。
示例 4:

输入: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
输出: 8
解释: 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。
注意: 答案在32位有符号整数的表示范围内。
'''
class Solution:
    def widthOfBinaryTree(self, root) -> int:
        import collections
        q = collections.deque([(root,0,0)])
        cur_depth = left = ans = 0
        while q:
            for _ in range(len(q)):
                node,depth,pos = q.popleft()
                if node:
                    q.append((node.left,depth+1,pos*2))
                    q.append((node.right, depth+1, pos*2+1))
                    if cur_depth !=depth:
                        cur_depth =depth
                        left=pos
                    ans = max(ans,pos-left+1)
        return ans
    def widthOfBinaryTree2(self, root) -> int:
        if not root: return 0
        max_width =1
        import collections
        q = collections.deque([(root,0)])
        while q:
            _, start = q[0]
            _, end = q[-1]
            for _ in range(len(q)):
                node,v = q.popleft()
                if node.left:
                    q.append((node.left,2*v))
                if node.right:
                    q.append((node.right,2*v+1))
            print(q)
            max_width = max(max_width,end-start+1)
        return max_width
                
            
if __name__ =='__main__':
    s= Solution()
    from src.common.tree import create_treenode
    root = create_treenode([1,3,2,5,3,None,9])
    print(root)
    print('1', s.widthOfBinaryTree(root))
    print('2', s.widthOfBinaryTree2(root))
    root = create_treenode([1,3,None,5,3])
    print(root)
    print('1', s.widthOfBinaryTree(root))
    print('2', s.widthOfBinaryTree2(root))
    root = create_treenode([1,3,2,5,None])
    print(root)
    print('1', s.widthOfBinaryTree(root))
    print('2', s.widthOfBinaryTree2(root))
    root = create_treenode(
        [1, 3, 2, 5, None, None, 9, 6, None, None, None, None, None,None, 7])
    print(root)
    print('1', s.widthOfBinaryTree(root))
    print('2', s.widthOfBinaryTree2(root))

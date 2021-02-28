#去重，标记访问过的节点
visited =set()
def process(node):
        pass
def generate_related_nodes(node):
        return 1
def bfs_temple(graph,start,end):
    q=[]
    q.append([start])
    visited.add(start)
    while q:
        node = q.pop()
        visited.add(node)
        #处理
        process(node)
        nodes = generate_related_nodes(node)
        # q.push(nodes)
#树的前序遍历、中序遍历、后序遍历都属于dfs
def dfs_temple1(node,tree):
    stack = []
    while stack:
        node = stack.pop()
        visited.add(node)
        process(node)
        nodes = generate_related_nodes(node)
        # stack.push(nodes)
        

def dfs_temple2(node,visited):
    visited.add(node)
    #process current here
    for next_node in node.children():
        if not next_node in visited:
            dfs_temple2(next_node,visited)

    
# def dfs_temple():
if __name__ =='__main__':
    q = [1,3]
    print(q.pop(0))
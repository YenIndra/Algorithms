from collections import deque
#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

class Node:
    def __init__(self,info):
        self.left = None
        self.right = None
        self.info = info

def inorder(root):
    stack = deque([root])
    visited = set()
    ls = []
    while stack:
        node = stack.pop()
        if node is None:
            continue
        if node.info in visited:
            #print(node.info,end = ' ')
            ls.append(node.info)
            continue
        visited.add(node.info)
        stack.append(node.right)
        stack.append(node)
        stack.append(node.left)
    return ls

def swap(root, k):
    """Don't use recursion b/c of recursion limit."""
    q = deque([(root, 1)])
    while q:
        node, level = q.popleft()
        if node is None:
            continue
        if level % k == 0:
            node.left, node.right = node.right, node.left
        q.append((node.left, level+1))
        q.append((node.right, level+1))





#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    #
    # Write your code here.
    from queue import Queue
    root = Node(1)
    q = Queue()

    q.put(root)
    for item in indexes:
        toadd = q.get()
        if item[0] != -1:
            toadd.left = Node(item[0])
            q.put(toadd.left)
        if item[1]!=-1:
            toadd.right = Node(item[1])
            q.put(toadd.right)

    result = []
    for eachquery in queries:
        swap(root,eachquery)
        rs = inorder(root)
        result.append(rs)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

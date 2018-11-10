
import collections

class Vertex:
    def __init__(self, id=None):
        self.id = id
        self.edges = []

# DO NOT EDIT
# generate graph from int and list of lists
def deserialize(n, edges):
    vertices = {}
    while n > 0:
        n -= 1
        vertices[n] = Vertex(n)
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        vertices[v1].edges.append(vertices[v2])
        vertices[v2].edges.append(vertices[v1])

    # UNCOMMENT OUT THIS AREA IF YOU WOULD LIKE TO SEE THE GRAPH YOU'VE BUILT:
    #
    '''
    for vertex_key in vertices:
        vertex = vertices[vertex_key]
        print('\nID: ' + str(vertex.id))
        for edge in vertex.edges:
            print('Edge ID: ' + str(edge.id))
    '''
    return vertices[0]


# sample_graph is the vertex with id 0
sample_graph = deserialize(8, [[0, 1], [1, 2], [2, 4], [3, 5], [4, 5], [1, 7], [4, 6], [4, 7], [5, 6]])

print("bfs")

def bfs(vertex, target):
  visited = set()
  queue = collections.deque()
  queue.append(vertex)
  visited.add(vertex.id)
  current = -1
  while len(queue) > 0:
    current = queue.popleft()
    if current.id == target:
      return current
    for edge in current.edges:
      if edge.id not in visited:
        visited.add(edge.id)
        queue.append(edge)
    print(current.id)
  return None

bfs(sample_graph, 3)

print("\ndfs")

def dfs(vertex, target):
  visited = set()
  stack = []
  stack.append(vertex)
  visited.add(vertex.id)
  while len(stack) > 0:
    current = stack.pop()
    if current.id == target:
      return current
    for edge in current.edges:
      if edge.id not in visited:
        visited.add(edge.id)
        stack.append(edge)
    print(current.id)
  return None


dfs(sample_graph, 3)
#
#  Target Practice 09 - Graph Traversal
#
#  Instructions: One of the most fundamental components of working with trees
#                and graphs is traversals.  We will focus primarily on this
#                piece to build your foundation of these data structures.
#
#
#
#  1. For the example graph below, what is the expected output if we printed
#     each vertex value from vertex 0 outwards using:
#
#     a. BREADTH FIRST traversal:
#     b. DEPTH FIRST traversal:
#
#     NOTE: Assume the order of edges will be in numerical order. E.g., Vertex
#           4 has edges to 5 vertices in the following order: 2, 5, 6, 7
#
#     NOTE: The traversal should take care of redundancy and not print the same
#           vertex value twice.
#
#     Example Graph:
#
#              2
#            /   \
#    0 ~~~ 1       4  ~~~ 5 ~~~ 3
#            \   /   \   /
#              7       6
#

# DO NOT EDIT
# Vertex class for a graph vertex
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
    # for vertex_key in vertices:
    #     vertex = vertices[vertex_key]
    #     print('\nID: ' + str(vertex.id))
    #     for edge in vertex.edges:
    #         print('Edge ID: ' + str(edge.id))
    return vertices[0]


# sample_graph is the vertex with id 0
sample_graph = deserialize(8, [[0, 1], [1, 2], [2, 4], [3, 5], [4, 5], [1, 7], [4, 6], [4, 7], [5, 6]])

#
#  1. Implement Breadth First Search using a queue and while loop.
#
#  Input: {Vertex} - the starting vertex
#  Output: {Array} - an array of vertex ids of the path
#
#  NOTE: You may use an array or linked list for your queue.
#
#  HINT: Use a hash table to handle redundancy
#

import collections


def bfs(vertex):
    visited = set()
    current = vertex
    path = []
    q = collections.deque()
    q.append(current)

    while not q.empty():
        current = q.popleft()
        print(path)
        if current.id not in visited:
            visited.add(current.id)
            path.append(current.id)
            for v in current.edges:
                q.put(v)

    return path


#
#  2. Implement Depth First Search using a stack and while loop.
#
#  Input: {Vertex} - the starting vertex
#  Output: {Array} - an array of vertex ids of the path
#
#  NOTE: You may use an array for your stack.
#
#  HINT: Use a hash table to handle redundancy
#


def dfs(vertex):
    pass


############################################################
###############  DO NOT TOUCH TEST BELOW!!!  ###############
############################################################

# custom assert function to handle tests
# input: count {List} - keeps track out how many tests pass and how many total
#        in the form of a two item array i.e., [0, 0]
# input: name {String} - describes the test
# input: test {Function} - performs a set of operations and returns a boolean
#        indicating if test passed
# output: {None}
def expect(count, name, test):
    if (count is None or not isinstance(count, list) or len(count) != 2):
        count = [0, 0]
    else:
        count[1] += 1

    result = 'false'
    error_msg = None
    try:
        if test():
            result = ' true'
            count[0] += 1
    except Exception as err:
        error_msg = str(err)

    print('  ' + (str(count[1]) + ')   ') + result + ' : ' + name)
    if error_msg is not None:
        print('       ' + error_msg + '\n')


# code for checking if lists contain the same elements
def lists_matching(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    cache = {}
    for i in range(0, len(lst1)):
        if lst1[i] in cache:
            cache[lst1[i]] += 1
        else:
            cache[lst1[i]] = 1
    for j in range(0, len(lst2)):
        if lst2[j] not in cache or cache[lst2[j]] == 0:
            return False
        cache[lst2[j]] -= 1
    return True


def get_neighbors(vertex, visited):
    edges = vertex.edges
    return list(filter((lambda edge: edge.id not in visited), edges))


def get_values(vertices):
    return list(map((lambda vertex: vertex.id), vertices))


# takes in a path list and a vertex start point and determines whether
# the bfs is valid
def valid_bfs(path, start):
    if path[0] != start.id:
        return False
    current = start
    visited = {}
    visited[current.id] = current
    i = 0
    j = 1
    while i < len(path):
        if i >= j:
            return False
        neighbors = get_neighbors(current, visited)
        values = get_values(neighbors)
        if not lists_matching(values, path[j:j + len(values)]):
            return False
        j += len(values)
        for vertex in neighbors:
            visited[vertex.id] = vertex
        if i + 1 in path:
            current = visited[path[i + 1]]
        i += 1
    return True


# compare if two flat lists are equal
def lists_equal(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(0, len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True


test_graph = deserialize(8, [[0, 1], [1, 2], [2, 4], [3, 5], [4, 5], [1, 7], [4, 6], [4, 7], [5, 6]])

print('breadth_first tests')
test_count = [0, 0]


def test():
    results = bfs(test_graph)
    return valid_bfs(results, test_graph)


expect(test_count, 'able to return the elements of a graph in breadth first manner', test)


def test():
    no_edge_graph = deserialize(8, [])
    results = bfs(no_edge_graph)
    return valid_bfs(results, no_edge_graph)


expect(test_count, 'should return only starting initial node if no edges exist in graph', test)


def test():
    simple_graph = deserialize(3, [[0, 1], [1, 2]])
    results = bfs(simple_graph)
    return valid_bfs(results, simple_graph)


expect(test_count, 'should return elements of a simple graph: 0 - 1 - 2 starting at 0', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

print('depth_first tests')
test_count = [0, 0]


def test():
    results = dfs(test_graph)
    return lists_equal(results, [0, 1, 7, 4, 6, 5, 3, 2]) or lists_equal(results, [0, 1, 2, 4, 5, 3, 6, 7])


expect(test_count, 'able to return the elements of a graph in depth first manner', test)


def test():
    no_edge_graph = deserialize(8, [])
    results = dfs(no_edge_graph)
    return lists_equal(results, [0])


expect(test_count, 'should return only starting initial node if no edges exist in graph', test)


def test():
    simple_graph = deserialize(3, [[0, 1], [1, 2]])
    results = dfs(simple_graph)
    return lists_equal(results, [0, 1, 2])


expect(test_count, 'should return elements of a simple graph: 0 - 1 - 2 starting at 0', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
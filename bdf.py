import queue

#
#  Target Practice 07 - BST Traversal
#

# DO NOT EDIT
# Node class for a binary tree node
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


# DO NOT EDIT
# generate tree from list
def deserialize(lst):
    if len(lst) == 0:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        if i + 1 < len(lst) and lst[i + 1] is not None:
            current.right = TreeNode(lst[i + 1])
            queue.append(current.right)
        i += 2
    return root


#
# Deserialize operates by building out the tree in a breadth-first
# manner. One only needs to build down to the lowest row where there
# exists nodes. For example, in this tree,
#
#          1
#            \
#              3
#             /
#            2
#
# The list that you would pass in to the deserialize function would
# be [1,None,3,2,None]. The first None represents the left child of
# the 1 node, and the second None represents the right child of the 3 node.
#
#  1. Here, we have built out the following tree using deserialize:
#
#              4
#            /   \
#          2       5
#        /   \       \
#      1       3       7
#                    /   \
#                  6      8
#

# DO NOT EDIT
lst = [4, 2, 5, 1, 3, None, 7, None, None, None, None, 6, 8]

sample_tree = deserialize(lst)


#
#  2. Given the example output binary search tree from Problem 1, what would
#     the order of values printed be if we used:
#
#     a. BREADTH FIRST traversal:
#     b. PRE-ORDER DEPTH first traversal:
#     c. IN-ORDER DEPTH first traversal:
#     d. POST-ORDER DEPTH first traversal:


#
#  3a. Using a queue, and while loop write a function that takes in a binary
#      search tree and outputs a list of values ordered by BREADTH FIRST
#      traversal.
#
#  Input: node {TreeNode}
#  Output: {List}
#
#  NOTE: You may use a list or linked list for your queue.
#  NOTE: Confirm with your answer from problem 2a.
#


def bfs(node):
    if node is None: return []
    result = []
    q = queue.Queue()
    q.put(node)
    while not q.empty():
        current = q.get()
        result.append(current.value)
        if current.left: q.put(current.left)
        if current.right: q.put(current.right)
    return result

#
#  3b. Using recursion, write a function that takes in a binary search tree and
#      outputs a list of values ordered by PRE-ORDER DEPTH FIRST traversal.
#
#      Input: node {TreeNode}
#      Output: {List}
#
#      NOTE: Confirm with your answer from problem 2b.
#


def dfs_pre(node):
    # YOUR WORK HERE
    pass

#
#  3c. Using recursion, write a function that takes in a binary search tree and
#      outputs a list of values ordered by IN-ORDER DEPTH FIRST traversal.
#
#      Input: node {TreeNode}
#      Output: {List}
#
#      NOTE: Confirm with your answer from problem 2c.
#


def dfs_in(node):
    # YOUR WORK HERE
    pass

#
#  3d. Using recursion, write a function that takes in a binary search tree and
#      outputs a list of values ordered by POST-ORDER DEPTH FIRST traversal.
#
#      Input: Binary Search Tree
#      Output: List
#
#      NOTE: Confirm with your answer from problem 2d.
#


def dfs_post(node):
    # YOUR WORK HERE
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

# code for capturing print output


from io import StringIO
import sys


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout

# code for checking if lists are equal
def lists_equal(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(0, len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True


# generate test tree for the rest of the tests
test_tree = TreeNode(4)
test_tree.left = TreeNode(2)
test_tree.left.left = TreeNode(1)
test_tree.left.right = TreeNode(3)
test_tree.right = TreeNode(5)
test_tree.right.right = TreeNode(7)
test_tree.right.right.left = TreeNode(6)
test_tree.right.right.right = TreeNode(8)


print('Problem 1 tests')
test_count = [0, 0]


def test():
    return not(sample_tree is None) and sample_tree.value == 4 and sample_tree.left.value == 2 and sample_tree.left.left.value == 1 and sample_tree.left.right.value == 3 and sample_tree.right.value == 5 and sample_tree.right.right.value == 7 and sample_tree.right.right.left.value == 6 and sample_tree.right.right.right.value == 8


expect(test_count, 'able to build tree as indicated in diagram', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('breadth first search tests')
test_count = [0, 0]


def test():
    results = bfs(test_tree)
    return not(results is None) and lists_equal(results, [4, 2, 5, 1, 3, 7, 6, 8])


expect(test_count, 'able to return values of BST in breadth first manner - [4,2,5,1,3,7,6,8]', test)


def test():
    results = bfs(deserialize([]))
    return not(results is None) and lists_equal(results, [])


expect(test_count, 'returns an empty erray for an empty BST', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('pre-order depth first search tests')
test_count = [0, 0]


def test():
    results = dfs_pre(test_tree)
    return not(results is None) and lists_equal(results, [4, 2, 1, 3, 5, 7, 6, 8])


expect(test_count, 'able to return values of BST in pre-order depth first manner - [4,2,1,3,5,7,6,8]', test)


def test():
    results = dfs_pre(deserialize([]))
    return not(results is None) and lists_equal(results, [])


expect(test_count, 'returns an empty erray for an empty BST', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('in-order depth first search tests')
test_count = [0, 0]


def test():
    results = dfs_in(test_tree)
    return not(results is None) and lists_equal(results, [1, 2, 3, 4, 5, 6, 7, 8])


expect(test_count, 'able to return values of BST in an in-order depth first manner - [1,2,3,4,5,6,7,8]', test)


def test():
    results = dfs_in(deserialize([]))
    return not(results is None) and lists_equal(results, [])


expect(test_count, 'returns an empty erray for an empty BST', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('post-order depth first search tests')
test_count = [0, 0]


def test():
    results = dfs_post(test_tree)
    return not(results is None) and lists_equal(results, [1, 3, 2, 6, 8, 7, 5, 4])


expect(test_count, 'able to return values of BST in post-order depth first manner - [1,3,2,6,8,7,5,4]', test)


def test():
    results = dfs_post(deserialize([]))
    return not(results is None) and lists_equal(results, [])


expect(test_count, 'returns an empty erray for an empty BST', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
import random
import sys
import json
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Definition for a binary tree node.

# total arguments
n = sys.argv


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []

        while (root != None or stack != None):

            while (root != None):
                stack.append(root)
                root = root.left

            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

        return res


def createTestCases(cant: int = 100):
    testCases = []
    posibles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, None]
    for i in range(cant):
        testCases.append(random.sample(posibles, 5))
    return testCases


# with open(n[1], 'w') as f:
#     testCases = createTestCases()
#     for i in range(len(testCases)):
#         f.write(str(json.dumps(testCases[i])) + '\n')

def to_binary_tree(items):
    if not items:
        return None

    it = iter(items)
    root = TreeNode(next(it))
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
    return root


with open(n[1], 'r') as f:
    testCases = f.readlines()
    for i in range(len(testCases)):
        test = json.loads(testCases[i].strip())
        if test[0] != None:
            root = to_binary_tree(test)
            print(Solution().inorderTraversal(root))

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        c_start=cloned
        stack=[c_start]
        while stack:
            node=stack.pop()
            if node.val==target.val:
                return node
            if node.left:stack.append(node.left)
            if node.right:stack.append(node.right)
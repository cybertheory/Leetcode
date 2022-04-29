# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        heap = [root]
        ans = 0
        if not root:
            return ans
        while heap:
            ans += 1
            count = len(heap)
            for i in range(count):
                node = heap.pop(0)
                if node.right:
                    heap.append(node.right)
                if node.left:
                    heap.append(node.left)
        return ans
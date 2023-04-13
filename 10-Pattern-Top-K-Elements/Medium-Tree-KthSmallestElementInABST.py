'''
Leetcode: 230. Kth Smallest Element in a BST
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/qZmOkDZ32E2

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    res = []
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)
    
    inorder(root)
    return res[k-1]


''' 
TC -> O(n) where n is the number of nodes in the BST 
SC -> O(n) we used a 'res' list of n nodes
'''
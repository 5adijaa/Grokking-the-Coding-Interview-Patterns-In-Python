'''
Leetcode: 337. House Robber III
Educative: educative.io/courses/grokking-coding-interview-patterns-python/B8KOZ3vwnDQ

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

Example 1:
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7. The thief cannot rob the houses that are connected with an edge, but can still rob the houses that are 
neighbors of the immediately adjacent houses.
     3
    / \ 
    2  3
    \   \ 
     3   1

Example 2:
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
'''
import math
from typing import Optional
from BinaryTree import *

       
def rob(root: Optional[BinaryTreeNode]) -> int:
    # Returns a tuple with max money for two scenarios: (withRoot, withoutRoot)
    # 1. withRoot: current node (root) is included in the sum
    # 2. withoutRoot: current node (root) is excluded from the sum

    def dfs(node):
        if not node:
            return (0,0)
        
        leftPair = dfs(node.left)
        rightPair = dfs(node.right)

        # If curr node (root) is included, we can't use its children at [0]
        withRoot = node.val + leftPair[1] + rightPair[1]

        # If curr node is excluded, we can choose whether to use its children or not
        withoutRoot = max(leftPair) + max(rightPair)

        return (withRoot, withoutRoot)
    
    return max(dfs(root))


def main():
    input1 = [3, 2, 3, None, 3, None, 1]
    tree1 = BinaryTree(input1)

    input2 = [3, 4, 5, 1, 3, None, 1]
    tree2 = BinaryTree(input2)

    input3 = [8, 2, 17, 1, 4, 19, 5]
    tree3 = BinaryTree(input3)

    input4 = [7, 3, 4, 1, 3]
    tree4 = BinaryTree(input4)

    input5 = [9, 5, 7, 1, 3]
    tree5 = BinaryTree(input5)


    inputTrees = [tree1.root, tree2.root, tree3.root, tree4.root, tree5.root]
    x = 1
    for i in inputTrees:
        print(x, ".\tInput Tree:", sep = "")
        display_tree(i)
        x+=1
        print("\tMaximum amount we can rob without getting caught: ", rob(i), sep = "")
        print("-" * 100)

if __name__ == "__main__":
    main()

'''
TC -> O(n), where n is the number of nodes in this tree. This is because the function performs a depth-first-search on the binary tree, visiting each node exactly once
SC -> O(h), where h is the height of the binary tree. This is because the dfs function is called recursively on the left and right children of each node until it reaches the leaf nodes. The maximum depth of the recursion stack is equal to the height of the tree.
'''
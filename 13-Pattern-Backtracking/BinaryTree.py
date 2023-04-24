from collections import *

class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

        # below val members used only for some of the problems
        self.next = None
        self.parent = None
        self.count = 0

class BinaryTree:
    # constructor
    def __init__(self, *args):
        if len(args) < 1:
            self.root = None
        elif isinstance(args[0], int):
            self.root = BinaryTreeNode(args[0])
        else:
            self.root = None
            self.insertList(args[0])

    # function to create the binary tree given a list of integers
    def insertList(self, inputList):
        if not inputList:
            self.root = None
        else:
            self.root = BinaryTreeNode(inputList[0])
            q = deque([self.root])
            i = 1
            while i < len(inputList):
                currentNode = q.popleft()
                if inputList[i] != None:
                    currentNode.left = BinaryTreeNode(inputList[i])
                    q.append(currentNode.left)
                i += 1
                if i < len(inputList) and inputList[i] != None:
                    currentNode.right = BinaryTreeNode(inputList[i])
                    q.append(currentNode.right)
                i += 1

    # function to find a node given the value stored in the node
    def find(self, value):
        q = deque([self.root])
        while q:
            currentNode = q.popleft()
            if currentNode:
                if currentNode.val == value:
                    return currentNode
                q.append(currentNode.left)
                q.append(currentNode.right)
            if all(val == None for val in q):
                break
        return None

    # function to return level order traversal of the binary tree
    def level_order_traversal(self):
        if not self.root:
            return []
        result = []
        q = deque([self.root])
        while q:
            currentNode = q.popleft()
            if currentNode:
                result.append(currentNode.val)
                q.append(currentNode.left)
                q.append(currentNode.right)
            else:
                result.append(None)
            if all(val == None for val in q):
                break
        return result

def display_tree(root):
    pass
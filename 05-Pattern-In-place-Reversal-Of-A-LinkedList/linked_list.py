#Definition for singly-linked list

# List Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    '''insertNodeAtHead method will insert a Linked ListNode at head of a linked list.'''
    def insertNodeAthead(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    '''createLL method will create the linked list using the
    given integer array with the help of InsertAthead method.'''
    def createLL(self, lst):
        for x in reversed(lst):
            new_node = ListNode(x)
            self.insertNodeAthead(new_node)
    
    '''__str__(self) method will display the elements of a linked list.'''
    def __str__(self):
        result = ''
        curr = self.head
        while curr:
            result += str(curr.val)
            curr = curr.next
            if curr:
                result += ', '
        result += ''
        return result


def print_list_with_forward_arrow(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.val, end=' ')  #print node value

        temp = temp.next
        if temp:
            print('→', end=' ')
        else:
            # if this is the last node, print null at the end
            print('→ null', end=' ')
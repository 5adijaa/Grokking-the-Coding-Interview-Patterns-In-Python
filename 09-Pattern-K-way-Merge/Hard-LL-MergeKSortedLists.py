'''
Leetcode: 23. Merge k Sorted Lists
https://www.educative.io/courses/grokking-coding-interview-patterns-python/R1DGRBzWY1w

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

'''
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition of Linked list class.
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

def merge2Lists(l1, l2):
    dummy = curr = ListNode()
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    if l1 or l2:
        curr.next = l1 if l1 else l2
    return dummy.next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    step = 1
    while step < len(lists):
        for i in range(0, len(lists)-step, 2*step): #Traverse over the lists in pairs
            l1 = lists[i].head
            l2 = lists[i+step].head
            lists[i].head = merge2Lists(l1, l2)
        step += 2
    
    return lists[0].head if len(lists)>0 else None

def main():
    inputlists = [
        [[21, 23, 42], [1, 2, 4]],
        [[11, 41, 51], [21, 23, 42]],
        [[2], [1, 2, 4], [25, 56, 66, 72]],
        [[11, 41, 51], [2], [2], [2], [1, 2, 4]],
        [[10, 30], [15, 25], [1, 7], [3, 9], [100, 300], [115, 125], [10, 70], [30, 90]]
    ]
    inp_num = 1
    for i in inputlists:
        print(inp_num, '.\tInput lists:', sep = '')
        ll_lists = []
        for x in i:
            a = LinkedList()
            a.createLL(x)
            ll_lists.append(a)
            print('\t', end = '')
            print_list_with_forward_arrow(a.head)
            print()
        inp_num += 1
        print('\tMerged list: \n\t', end = '')
        print_list_with_forward_arrow(mergeKLists(ll_lists))
        print('\n', '-'*80, sep = '')


if __name__ == '__main__':
    main()
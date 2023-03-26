'''
Leetcode: 24. Swap Nodes in Pairs
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/xlZB0J8k8wP

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Input: head = [1,2,3,4]
Output: [2,1,4,3]
'''

from typing import Optional
from linked_list import *

def swap(node1, node2):
    node1.val, node2.val = node2.val, node1.val


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0, next=head)
    prev = dummy

    while prev and prev.next:
        curr = prev.next
        i=1
        while curr and curr.next and i < 2:
            curr = curr.next
            i+=1
        swap(prev.next, curr)
        prev = curr
        # curr = curr.next
    
    return dummy.next


def main():
    linkedlists = [
        [1],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6, 7],
        [6, 9, 3, 10, 7, 4, 6],
        [6, 2, 3, 6, 9],
        [6, 2]
    ]

    for i in range(len(linkedlists)):
        linked_list = LinkedList()
        linked_list.createLL(linkedlists[i])

        print(i + 1, '.\tOriginal linked list is: ', end='')
        print_list_with_forward_arrow(linked_list.head)
        result = swapPairs(linked_list.head)
        print('\n\tSwap Nodes In Pairs: ', end='')
        print_list_with_forward_arrow(result)
        print('\n', '-'*100, sep='')


if __name__ == '__main__':
    main()


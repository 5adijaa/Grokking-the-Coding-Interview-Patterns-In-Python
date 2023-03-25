'''
Leetcode: 1721. Swapping Nodes in a Linked List
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/3Y6XPZEzD7M

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

My answer' steps:
- maintain a curr pointer to loop over the ll
- maintain 2 pointers, to find k-th first node from beginning and k-th last node from end.
- We go out from the loop with 'first' points at k-th node from beginning and 'last' at the k-th node from the end. last first needs to point at None. Once we reach the first k-th node we instantiate last to head and increment it as we loop.
'''

from typing import Optional
from linked_list import *

#  Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapNodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    curr = head
    last = None
    i = 1
    while curr:
        last = None if last == None else last.next #'last' will point at k-th node from end.

        if i == k:
            first = curr #'first' will point at k-th node from beginning
            last = head
        curr = curr.next
        i += 1

    # swap values
    first.val, last.val = last.val, first.val

    return head


def main():
    lists = [
        [1, 2, 3, 4, 5, 6, 7],
        [6, 9, 3, 10, 7, 4, 6],
        [6, 9, 3, 4],
        [6, 2, 3, 6, 9],
        [6, 2],
        [100, 90]
    ]
    k = [2, 3, 2, 3, 1, 2]

    for i in range(len(lists)):
        linked_list = LinkedList()
        linked_list.createLL(lists[i])
        print(i + 1, '.\tOriginal linked list is: ', end='')
        print_list_with_forward_arrow(linked_list.head)
        print('\n\tk:', k[i])
        if k[i] <= 0:
            print('\tThe expected "k" to have value from 1 \
            to length of the linked list only.')
        else:
            result = swapNodes(linked_list.head, k[i])
            print('\tLinked list with swapped values: ', end='')
            print_list_with_forward_arrow(result)
        print('\n', '-'*100, sep='')


if __name__ == '__main__':
    main()

'''
TC -> O(n) where n is the number of nodes in a linked list
SC -> O(1)
'''
'''
leetcode: 25. Reverse ListNodes in k-Group
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/mE6KynXWR8O

Given the head of a linked list, reverse the Listnodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of Listnodes is not a multiple of k then left-out Listnodes, in the end, should remain as it is.

You may not alter the values in the list's Listnodes, only Listnodes themselves may be changed.

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Input: head = [1,2,3,4,5,6,7], k = 3
Output: [3,2,1,6,5,4,7]
'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return str(self.val)
    
    def printLinkedList(self):
        curr = self
        while curr:
            print(curr.val, end =' -> ')
            curr = curr.next
        print('Null')


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #using a stack TC-> O(n) and SC-> O(n)
    reverse_head = ListNode()
    tmp = reverse_head
    stack = []
    curr = head
    while curr:
        stack.append(curr)
        if len(stack) == k:
            nxt = curr.next
            while stack:
                tmp.next = stack.pop()
                tmp = tmp.next
            tmp.next = nxt
            curr = nxt
        else:
            curr = curr.next
    return reverse_head.next


def main():
  head = ListNode(1)
  head.next = ListNode(2)
  head.next.next = ListNode(3)
  head.next.next.next = ListNode(4)
  head.next.next.next.next = ListNode(5)
  head.next.next.next.next.next = ListNode(6)
  head.next.next.next.next.next.next = ListNode(7)

  print('The original Linked List is: \t\t', end =' ')
  head.printLinkedList()
  k=3
  reversed_LL = reverseKGroup(head, k)
  print('\nReversed linked list, with k = ', k, ': \t', sep=' ', end=' ')
  reversed_LL.printLinkedList()

main()
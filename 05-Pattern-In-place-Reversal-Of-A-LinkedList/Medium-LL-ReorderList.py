'''
leetcode: 143. Reorder List
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/myzE6YZ7KQG

You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form: 
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Answer steps:
1. Find middle of LL
2. Reverse the 2nd half of the LL
3. Merge the 2 halfs of the LL
'''

from typing import Optional
from linked_list import LinkedList, print_list_with_forward_arrow

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head: Optional[ListNode]) -> None:
    slow = fast = head
    
    # 1. Find the middle node of our LL
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    prev = None
    curr = slow #Now, 'slow' points at the middle of LL
    
    # 2. Reverse the 2nd half of our LL
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    
    first = head
    second = prev #Now, 'prev' points at the Head of the 2nd half reversed LL

    # 3. Merge lists: Update the links between 1st half and 2nd reversed half
    while second.next:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2
    
    return head


def main():
    linked_lists = [
        [1,2,3,4],
        [1,2,3,4,5],
        [1, 1, 2, 2, 3, -1, 10, 12],
        [10, 20, -22, 21, -12],
        [1, 1, 1],
        [-2, -5, -6, 0, -1, -4],
        [3, 1, 5, 7, -4, -2, -1, -6]
    ]

    for i, list in enumerate(linked_lists):
        linked_list = LinkedList()
        linked_list.createLL(list)

        print(i+1, '- Original LinkedList: ', end=' ')
        print_list_with_forward_arrow(linked_list.head)
        print()

        print('Reorder the LinkedList: ', end='')
        reorder = reorderList(linked_list.head)
        print_list_with_forward_arrow(reorder)
        print()
        print('-'*75)

main()

'''
TC -> O(n) The time complexity of this solution is linear, where n is the number of nodes in the linked list. 
SC -> O(1) we didn't use any extra memory.
'''
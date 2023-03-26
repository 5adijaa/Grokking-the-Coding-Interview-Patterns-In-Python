'''
Leetcode: 2074. Reverse Nodes In Even Length Groups
Educative: 

You are given the head of a linked list.

The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). The length of a group is the number of nodes assigned to it. In other words:
- The 1st node is assigned to the first group.
- The 2nd and the 3rd nodes are assigned to the second group.
- The 4th, 5th, and 6th nodes are assigned to the third group, and so on.
Note that the length of the last group may be less than or equal to 1 + the length of the second to last group.

Reverse the nodes in each group with an even length, and return the head of the modified linked list.

Input: head = [5,2,6,3,9,1,7,3,8,4]
Output: [5,6,2,3,9,1,4,8,3,7]
Explanation:
- The length of the first group is 1, which is odd, hence no reversal occurs.
- The length of the second group is 2, which is even, hence the nodes are reversed.
- The length of the third group is 3, which is odd, hence no reversal occurs.
- The length of the last group is 4, which is even, hence the nodes are reversed.
'''
from typing import Optional
from linked_list import *

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def reverse(start, stop):
    prev = None
    curr = start
    while curr != stop:
        curr.next, prev, curr = prev, curr, curr.next
    return prev, start


def reverseEvenLengthGroups(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = head #will point at node before the start of the current group
    group_len = 1

    while prev and prev.next:
        group_len +=1
        start = end = prev.next 
        n = 1 #group number and use it to count its length
        while end and end.next and n < group_len: #help us to get 'end' node of curr group
            end = end.next
            n+=1
        
        next_end = end.next #will point at node after end of current group

        if n%2 != 0: #odd group -> do nothing, just update prev
            prev = end
        else: #even group -> reverse it
            new_head, new_tail = reverse(start, next_end)
            prev.next = new_head
            new_tail.next = next_end
            prev = new_tail #dont forget to update prev to point at end of curr group
    
    return head

def main():
    lists = [
        [5, 2, 6, 3, 9, 1, 7, 3, 8, 4],
        [1, 2, 3, 4],
        [10, 11, 12, 13, 14],
        [15],
        [16, 17]
    ]

    for i in range(len(lists)):
        linked_list = LinkedList()
        linked_list.createLL(lists[i])
        print( i+1, '.\tIf we reverse the even length groups of the linked list: ', end='\n\t')
        print_list_with_forward_arrow(linked_list.head)
        print('\n\n\tWe will get: ', end='\n\t')
        print_list_with_forward_arrow(
            reverseEvenLengthGroups(linked_list.head))
        print('\n')
        print('-' * 75)


if __name__ == '__main__':
    main()

'''
TC -> O(n)
SC -> O(1)
'''
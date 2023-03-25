'''
leetcode: 92. Reverse Linked List II
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/qVvv9BMnE52

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Input: head = [5], left = 1, right = 1
Output: [5]

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

'''
from typing import Optional
from linked_list import LinkedList, print_list_with_forward_arrow

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head):
    prev = None
    curr = tail = head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    return prev, tail


def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    # Create a dummy node to avoid edge cases + to make sure it points on the head
    dummy = ListNode(0, next=head)
    prev = dummy
    curr = head

    left_node = None #will point at node before 'left' index
    right_node = None #will point at node after 'right' index
    rev_head = None #will point at head of our subLL
    i = 1 

    while curr:
        if i == left:
            left_node = prev
            prev.next = None
            rev_head = curr #will point at our new subLl head -> to bereversed later
        if i == right:
            right_node = curr.next
            curr.next = None
        i += 1
        prev = curr
        curr = curr.next
    
    # reverse my subLL delimited by left and right indices
    new_head, new_tail = reverse(rev_head)

    # reconnect the reversed subLL with our LL:
    left_node.next = new_head
    new_tail.next = right_node

    return dummy.next
    

def main():
    linkedlists = [
        [1,2,3,4,5],
        [1, 2, 3, 4, 5, 6, 7],
        [6, 9, 3, 10, 7, 4, 6],
        [6, 9, 3, 4],
        [6, 2, 3, 6, 9],
        [6, 2]
    ]
    left = [2, 1, 3, 2, 1, 1]
    right = [4, 5, 6, 4, 3, 2]

    for i in range(len(linkedlists)):
        linked_list = LinkedList()
        linked_list.createLL(linkedlists[i])

        print(i + 1, '.\tOriginal linked list is: ', end='')
        print_list_with_forward_arrow(linked_list.head)
        print(', left = ', left[i], ', right = ', right[i])
        if left[i] <= 0:
            print("\n\tThe expected 'left' and 'right' to have \
            value from 1 to length of the linked list only.")
        else:
            result = reverseBetween(linked_list.head, left[i], right[i])
            print('\n\tReversed linked list is: ', end='')
            print_list_with_forward_arrow(result)
        print('\n', '-'*100, sep='')


if __name__ == '__main__':
    main()


'''
TC -> Each node will be processed at most one time. Hence, the time complexity will be O(n), where n is the number of nodes in the linked list
SC -> The space complexity will be O(1) because we didn't use any extra space, we used a constant number of additional variables to maintain the proper connections between the nodes during reversal
'''
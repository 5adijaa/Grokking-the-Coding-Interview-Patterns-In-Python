'''
leetcode: 206. Reverse Linked List
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/NELnLMDjKvD

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None 
    
    def insertNodeAtHead(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
    
    def createLinkedList(self, lst):
        for x in reversed(lst):
            new_node = ListNode(x)
            self.insertNodeAtHead(new_node)
    
    def __str__(self):
        result = ''
        temp = self.head
        while temp:
            result += str(temp.val)
            temp = temp.next
            if temp:
                result += ', '
        result += ''
        return result


def print_list_with_forward_arrow(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.val, end=' ')  # print node value
        
        temp = temp.next
        if temp:
            print('→', end=' ')
        else:
            # if this is the last node, print null at the end
            print('→ null')


def reverseLinkedList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next: #check if head is None or there is only 1 node.
        return head
    
    prev = None
    curr = head
    while curr:
        # curr.next, prev, curr = prev, curr, curr.next
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev
    


# Driver code:
def main():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8]
    input_linked_list = LinkedList()
    input_linked_list.createLinkedList(input_list)

    print('The original linked list:  ', end='')
    print_list_with_forward_arrow(input_linked_list.head)
    result = reverseLinkedList(input_linked_list.head)
    print('The reversed linked list:  ', sep='', end='')
    print_list_with_forward_arrow(result)


if __name__ == '__main__':
    main()

'''
TC -> O(n), where n is the total number of nodes in the Linked List
SC -> O(1), because no extra memory is required for the iterative solution.
'''
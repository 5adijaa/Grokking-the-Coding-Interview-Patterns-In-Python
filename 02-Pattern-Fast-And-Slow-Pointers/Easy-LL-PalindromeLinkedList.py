'''
Leetcode: 234. Palindrome Linked List
https://www.educative.io/courses/grokking-coding-interview-patterns-python/JYOEOpNo89K

Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false

'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def createLL(self, l):
        if not l:
            return None
        self.head = ListNode(l[0])
        curr = self.head
        for i in range(1, len(l)):
            curr.next = ListNode(l[i])
            curr = curr.next
        return self
    
    def printLL(self, head, length):
        curr = head
        i = 0
        while curr and i < length:
            print(curr.val, '→ ', end='')
            curr = curr.next
            i += 1
        print('None')
    
    def getLength(self, head):
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        return length

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        ### Follow up Question: Could you do it in O(n) time and O(1) space? ###
        ## instead of using a stack => we use slow and fast pointers,
        ## TC -> O(n)
        ## SC -> O(1) : no extra space wes needed
        '''
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right = self.reverseLL(slow) #reverse slow not slow.next 
        left = head
        while right:
            if left.val == right.val:
                left = left.next
                right = right.next
            else:
                return False
        
        return True
    
    def reverseLL(self, head):
        prev = None
        curr = head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
    

def main():
    tests = (
        [1, 2, 2, 1],
        [1, 2],
        [0, 3, 5, 5, 0],
        [9, 7, 4, 4, 7, 9],
        [5, 4, 7, 9, 4, 5],
        [5, 9, 8, 3, 8, 9, 5],
    )

    for i in range(len(tests)):
        linked_list = LinkedList()
        linked_list.createLL(tests[i])
        print(f'Test:{i+1} -', 'Linked List: ', end=' ')

        length = linked_list.getLength(linked_list.head)
        linked_list.printLL(linked_list.head, length)
        
        print('\n\tIs it a palindrome? =>', end=' ')
        print(linked_list.isPalindrome(linked_list.head))
        print('-'*55, '\n')


if __name__ == '__main__':
    main()
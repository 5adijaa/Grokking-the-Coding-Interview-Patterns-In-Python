'''
Leetcode 141. Linked List Cycle
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/YM8j7LYjZOp

Problem:
Check if a linked list contains a cycle or not. If a cycle exists, return TRUE. Otherwise, return FALSE.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
'''

from typing import List, Optional

# Node Class
class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

# LinkedList Class
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def createLLFromList(self, lst):
        '''Creates a linkedlist from a given list'''
        if not lst: #empty list
            return self
        
        self.head = ListNode(lst[0])
        tmp = self.head
        for i in range(1, len(lst)):
            tmp.next = ListNode(lst[i])
            tmp = tmp.next
        return self

    def printLinkedList(self, head, length):
        '''Prints the linked list with forward arrows'''
        # I added 'length' (length of the given list) to avoid printing infinite LL
        curr = head
        i=0
        while curr and i < length:
            print(curr.val, '→ ', end='')
            curr = curr.next
            i+=1
        print('Null')
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''Returns True if a LL has a cycle. Otherwise, returns False'''
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

    def getLength(self, head):
        '''Returns the number of nodes in the linkedlist '''
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        return length

    def getNode(self, head, pos):
        '''Returns the node at the specified position(index) of the linkedlist'''
        '''We will need this method on tests to check the cycle in a linkedlist'''
        if pos != -1:
            p = 0
            node = head
            while p < pos:
                node = node.next
                p += 1
            return node


def main():
    tests = (
        [3, 2, 0, -4],
        [1, 2],
        [1],
        [1, 3, 5, 7, 9, 11], 
        [5, 1, 4, 9, 2, 3]
    )
    pos = [1 , 0, -1, -1, 2]

    for i in range(len(tests)):
        linked_list = LinkedList()
        linked_list.createLLFromList(tests[i])
        length = linked_list.getLength(linked_list.head)
        # print(length)
        if pos[i] != -1:
            last_node = linked_list.getNode(linked_list.head, length-1)
            last_node.next = linked_list.getNode(linked_list.head, pos[i])

        print('-'*50)
        print(f'Test Nº: {i} - LL: ', end ='')
        linked_list.printLinkedList(linked_list.head, length)
        print('Processing...')
        print(f'\nDetected cycle = {linked_list.hasCycle(linked_list.head)}\n')

main()

'''
TC -> O(n): In the worst case, the loop runs n-1 times as the slow pointer goes from the first to the penultimate node. Each loop iteration has O(1) steps
SC -> O(1) because it requires a constant number of additional variables.
'''
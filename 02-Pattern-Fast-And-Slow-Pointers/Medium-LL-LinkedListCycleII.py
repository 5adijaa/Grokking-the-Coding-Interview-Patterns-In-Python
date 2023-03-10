'''
Leetcode: 142. Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null (None in Python).

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
‼️ Do not modify the linked list.

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
'''

from typing import Optional


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head
    
    def createLLFromList(self, lst):
        if not lst: 
            return self
        self.head = Node(lst[0])
        curr = self.head
        i=1
        while i < len(lst):
            curr.next = Node(lst[i])
            curr = curr.next
            i += 1
        return self
    
    def printLL(self, head, length):
        curr = head
        i = 0
        while curr and i < length:
            print(curr.val, '→ ', end='')
            curr = curr.next
            i += 1
        print('None')
    
    def detecteCycle(self, head: Optional[Node]) -> Optional[Node]:
        fast, slow = head, head
        cycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                cycle = True
                break
        else:
            return None
        
        if cycle:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            # return slow
            return slow.val
    
    def getLength(self, head):
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        return length
    
    def getNode(self, head, pos):
        if pos != -1:
            i = 0
            curr = head
            while i < pos:
                curr = curr.next
                i += 1
            return curr

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
        print('-'*50)
        linked_list = LinkedList()
        linked_list.createLLFromList(tests[i])
        length = linked_list.getLength(linked_list.head)
        print(f'Test Nº:{i+1} -- LL: ', end ='')
        linked_list.printLL(linked_list.head, length)
        print('pos =', pos[i])
        if pos[i] != -1:
            last_node = linked_list.getNode(linked_list.head, length-1)
            last_node.next = linked_list.getNode(linked_list.head, pos[i])
            print('Tail connects to node index:', linked_list.detecteCycle(linked_list.head))
        else:
            print('No cycle detected')
        print('-'*50)


main()
'''
Leetcode: 876. Middle of the Linked List

Given a singly linked list, return the middle node of the linked list. 
If the number of nodes in the linked list is even, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
'''

# singly-linked list.
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

    def getMiddleNode(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # return slow
        return slow.val
    


def main():
    tests = (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [3, 2, 1],
        [10],
        [1, 2],
    )

    for i in range(len(tests)):
        linked_list = LinkedList()
        linked_list.createLL(tests[i])
        
        print(i+1, '.\tLinked list: ', sep='', end='')
        length = linked_list.getLength(linked_list.head)
        linked_list.printLL(linked_list.head, length)
        
        print('\n\tMiddle of the linked list: ', 
              linked_list.getMiddleNode(linked_list.head))
        print('-'*100, '\n')


if __name__ == '__main__':
    main()

'''
TC -> O(n): where n is the number of nodes in the linked list
SC -> O(1)
'''
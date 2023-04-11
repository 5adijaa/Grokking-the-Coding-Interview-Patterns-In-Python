'''
Leetcode: 703. Kth Largest Element in a Stream
Educative: https: ww.educative.io/courses/grokking-coding-interview-patterns-python/xoW1VrXA3mJ

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

- KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
- int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Input
['KthLargest', 'add', 'add', 'add', 'add', 'add']
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);    return 4
kthLargest.add(5);    return 5
kthLargest.add(10);   return 5
kthLargest.add(9);    return 8
kthLargest.add(4);    return 8
'''
from typing import List
from heapq import *

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)
        while len(self.heap) > k: #pop from the heap until the heap size is = k
            heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k: #if the size exceeds k, pop from the heap.
            heappop(self.heap)
        print('\tNew heap: ', self.heap)
        return self.heap[0]
    

def main():
    nums = [4, 5, 8, 2]
    temp = [4, 5, 8, 2]
    print('\tInitial stream= ', nums, 'and k = ', 3, sep = '')
    KLargest = KthLargest(3, nums)
    val = [3, 5, 10, 9, 4]
    print()
    for i in range(len(val)):
        print('\tAdding a new number ', val[i], ' to the stream', sep = '')
        temp.append(val[i])
        print('\tNumber stream: ', temp, sep = '')
        print('\tKth largest element in the stream: ', KLargest.add(val[i]))
        print('-'*75)

main()

'''
TC -> 
- The time complexity of the constructor is O(nlogk) where n is the length of the input nums list. This is because we are adding each element to the heap and then popping the smallest element if the heap size is greater than k.
- The time complexity of adding an element to the heap is O(logk) because we are maintaining a heap of size k
SC -> The space complexity of the class KthLargest is O(k) because the heap only stores the k largest elements
'''
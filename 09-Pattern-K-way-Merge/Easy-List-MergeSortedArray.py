'''
Leetcode: 88. Merge Sorted Array
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/gxWjRVqvQEj

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
'''
from typing import List
from heapq import *

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    '''
    Do not return anything, modify nums1 in-place instead.
    '''
    min_heap = []

    for p1 in range(m):
        heappush(min_heap, nums1[p1])
    
    for p2 in range(n):
        heappush(min_heap, nums2[p2])
    
    i = 0
    while min_heap and i < n+m:
        nums1[i] = heappop(min_heap)
        i+=1
    
    return nums1

'''
TC -> O((m+n)log(m+n)), where m and n are the lengths of the input arrays nums1 and nums2, respectively. This is because our algorithm first pushes all elements from nums1 and nums2 into a min heap, which takes O(m+n) time. Then, it pops elements from the heap and assigns them to nums1, which takes O((m+n)log(m+n)) time.
SC -> O(m+n) because we created a min heap of size m+n to store all the elements from nums1 and nums2
'''


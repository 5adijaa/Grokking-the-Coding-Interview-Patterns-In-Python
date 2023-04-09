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
    # Follow up: Can you come up with an algorithm that runs in O(m + n) time?
    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    return nums1

def main():
    m = [3, 1, 0, 9, 2, 3, 1, 8]
    n = [3, 0, 1, 6, 1, 4, 2, 1]
    nums1 = [
        [1, 2, 3, 0, 0, 0],
        [1],
        [0],
        [23, 33, 35, 41, 44, 47, 56, 91, 105, 0, 0, 0, 0, 0, 0], 
        [1, 2, 0], 
        [1, 1, 1, 0, 0, 0, 0], 
        [6, 0, 0], 
        [12, 34, 45, 56, 67, 78, 89, 99, 0]
    ]
    nums2 = [
        [2, 5, 6],
        [],
        [1],
        [32, 49, 50, 51, 61, 99], 
        [7], 
        [1, 2, 3, 4], 
        [-99, -45], 
        [100]
    ]
    k = 1
    for i in range(len(m)):
        print(k, '.\tnums1: ', nums1[i], ', m: ', m[i], sep = '')
        print('\tnums2: ', nums2[i], ', n: ', n[i], sep = '')
        print('\n\tMerged list: ', merge(nums1[i], m[i], nums2[i], n[i]), sep = '')
        print('-'*100, '\n')
        k += 1


if __name__ == '__main__':
    main()

'''
TC -> O(m+n), where m and n are the lengths of the input arrays nums1 and nums2, respectively.
SC -> O(1)
'''


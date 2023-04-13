'''
215. Kth Largest Element in an Array
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/m2XNwP9G7LA

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''
from heapq import heappop, heappush
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    min_heap = []

    for i in range(k):
        heappush(min_heap, nums[i])
    
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[i])
    
    return min_heap[0]


def main():
    input_list = [
        [3, 2, 1, 5, 6, 4],
        [3, 2, 3, 1, 2, 4, 5, 5, 6],
        [1, 5, 12, 2, 11, 9, 7, 30, 20], 
        [23, 13, 17, 19, 10], 
        [3, 2, 5, 6, 7], 
        [1, 4, 6, 0, 2], 
        [1, 2, 3, 4, 5, 6, 7]
    ]
    k_list = [2, 4, 3, 4, 5, 1, 7]
    for i in range(len(input_list)):
        print(i + 1, '.\tNums =', input_list[i], ', k = ', k_list[i])
        print('\tkth largest number is: ', findKthLargest(input_list[i], k_list[i]))
        print('-'*100)


if __name__ == '__main__':
    main()

'''
TC -> 
The first loop inserts k elements into a list, which takes O(k) time complexity. Heapifying this list takes O(k) time complexity as well.
In the worst case, in the second loop, we may be pushing n-k elements on to the heap, where n is the size of the input list. Each push and pop operation takes logk time, so n-k items being pushed results in O(n-k)logk) time complexity.
The overall time complexity is thus O(k+(n-k)logk) which simplifies to O((n-k)logk) .
SC ->
The space complexity is O(k) because we are storing k elements in the heap.
'''
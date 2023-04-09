'''
Leetcode: 378. Kth Smallest Element in a Sorted Matrix
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/JYAvqALoGE9

Given n number of sorted lists in ascending order and an integer k , find the k-th smallest number among all the given lists.

Constraints:
- If k is greater than the total number of elements in the input lists, return the greatest element from all the lists.
- If there are no elements in the input lists, return 0.
- You must find a solution with a memory complexity better than O(n^2)

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Input: matrix = [[-5]], k = 1
Output: -5

'''
from typing import List
from heapq import *

def kthSmallest(matrix: List[List[int]], k: int) -> int:
    min_heap = []
    n = len(matrix)

    # Initialize a min heap and add the first element from each row to the heap.
    for i in range(n):
        if matrix[i] == []: #check if lists are empty: [[],[],[]] -> return []
            continue
        heappush(min_heap, (matrix[i][0], i, 0))
    
    # While the heap is not empty, pop the smallest element from the heap. 
    # check if numbers_checked = k so break loop and return k-th smallest element (but if k>n smallest_num will return the max elt in the matrix)
    # otherwise, insert the next element from the same row into the heap.
    smallest_num, numbers_checked = 0, 0
    while min_heap:
        smallest_num, row, col = heappop(min_heap)
        k -= 1 
        if k == numbers_checked:
            break
        if col + 1 < len(matrix[row]):
            heappush(min_heap, (matrix[row][col+1], row, col+1))
    
    return smallest_num


def main():
    lists = [
        [[1,5,9],[10,11,13],[12,13,15]],
        [[-5]],
        [[2, 6, 8], [3,6,10], [5, 8, 11]],
        [[1, 2, 3], [4, 5], [6, 7, 8, 15], [10, 11, 12, 13], [5, 10]],
        [[], [], []],
        [[1, 1, 3, 8], [5, 5, 7, 9], [3, 5, 8, 12]],
        [[5, 8, 9, 17], [], [8, 17, 23, 24]]
    ]
    k = [8, 1, 5, 50, 7, 4, 8]

    for i in range(len(k)):
        print(i + 1, '.\t Input lists: ', lists[i],
              f'\n\t K = {k[i]}',
              f'\n\t {k[i]}th smallest number from the given lists is: ',
              kthSmallest(lists[i], k[i]), sep='')
        print('-' * 100)


if __name__ == '__main__':
    main()

    
'''
-> TC is o((k+n)logn) because:
- In the for loop, the Cost of pushing n elements onto the heap is: log1+log2+log3+⋯+log(n)=log(1*2*3...*n)=log(n!)tha is approximatively: O(logn!) ≈ O(nlogn)
- In the while-loop, we pop and push on to the heap k number of times until we find the k-th smallest number. So, the time complexity of this step is O(klogn).
So the whole TC: is O((k+n)logn)
-> SC: O(n) to store n elements from each list in the min-heap.
'''
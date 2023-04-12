'''
Leetcode: 347. Top K Frequent Elements
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/m7rGqMPRkDn

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
'''
from collections import Counter
from typing import List
from heapq import *


def topKFrequent(nums: List[int], k: int) -> List[int]:
    min_heap = []*k
    frequency_map = Counter(nums)

    for num, frequency in frequency_map.items():
        heappush(min_heap, (frequency, num))
        if len(min_heap) > k:
            heappop(min_heap)

    res = []
    while min_heap:
        res.append(heappop(min_heap)[1])
    
    return res


def main():
    nums_lists = [
        [1,1,1,2,2,3],
        [1, 3, 5, 12, 11, 12, 11, 12, 5], 
        [1, 3, 5, 14, 18, 14, 5],
        [2, 3, 4, 5, 6, 7, 7], 
        [9, 8, 7, 6, 5, 4, 3, 2, 1], 
        [2, 4, 3, 2, 3, 4, 5, 4, 4, 4], 
        [1, 1, 1, 1, 1, 1], 
        [2, 3]
    ]
    k_lists = [2, 3, 2, 1, 1, 3, 1, 2]

    for i in range(len(k_lists)):
        print(i+1, '. \t Input: ( nums = ', nums_lists[i], ', k = ', k_lists[i], ')')
        print('\t Top', k_lists[i], 'frequent Elements are: ',
              topKFrequent(nums_lists[i], k_lists[i]))
        print('-'*100)


if __name__ == '__main__':
    main()

'''
TC -> Let n be the number of elements in our list and k be the k elements . We're iterating through a list of size n, and it takes O(log(k)) time to insert the element into the heap. If k<n , the time complexity will be O(nlog(k)), and in the worst case, if k=n the time complexity will be O(nlog(n)).
SC -> O(n+k), where k is the size of the heap and n the size of the hashmap to store frequency.
'''
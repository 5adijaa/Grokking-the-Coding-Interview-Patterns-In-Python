'''
Leetcode: 373. Find K Pairs with Smallest Sums
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/xV99L9rXO1E

Given two lists, and an integer k, find k pairs of numbers with the smallest sum so that in each pair, each list contributes one number to the pair. 

Constraints: 
- Input lists should be sorted in ascending order. 
- If the value of k exceeds the total number of valid pairs that may be formed, return all the pairs.

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

'''
from typing import List
from heapq import *

def kSmallestPairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    min_heap = []
    pairs = []

    for i in range(len(nums1)):
        heappush(min_heap, (nums1[i]+nums2[0], i, 0))
    
    # print(min_heap)

    while min_heap and k>0:
        curr_sum_of_pairs, i, j = heappop(min_heap)
        pairs.append([nums1[i], nums2[j]])
        k-=1
        if j+1 < len(nums2):
            heappush(min_heap, (nums1[i]+nums2[j+1], i, j+1))
    
    return pairs


def main():
    list1 = [[1,7,11], [1, 1, 2], [2, 8, 9], [1, 2, 300], [4, 6], [4, 7, 9], [1, 1, 2]]
    list2 = [[2,4,6], [1, 2, 3], [1, 3, 6], [1, 11, 20, 35, 300], [2, 3], [4, 7, 9], [1]]

    k = [3, 2, 9, 30, 1, 5, 4]

    # loop to execute till the length of list k
    for i in range(len(k)):
        print(i + 1, '.\t Input pairs: ', list1[i], ', ', list2[i],
              f'\n\t k = {k[i]}', sep='')
        print('\t Pairs with the smallest sum are: ',
              kSmallestPairs(list1[i], list2[i], k[i]), sep='')
        print('-' * 100)


if __name__ == '__main__':
    main()


'''
TC -> The first round of pushing pairs onto the heap, with the first element of the second list fixed, takes O(mlogm) time, where m = min(k,len(nums1)). The second loop will run at most k times. Assuming that each iteration involves pushing onto the min-heap, its size will stay constant, that is m. Each push and pop operation therefore costs O(logm). So, the cost of the second loop is O(klogm). Therefore, the total time complexity of this algorithm is O((m+k)logm).
SC ->  The space complexity of this algorithm is O(m) , where m = min(k,len(nums1)).
'''
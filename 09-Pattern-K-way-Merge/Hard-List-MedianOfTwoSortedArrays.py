'''
Leetcode: 4. Median of Two Sorted Arrays.
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/m7Z33JoE51E

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)). !!!! Constraint !!!!

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5

'''
from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2): #We want nums1 to be the shorter list
        nums1, nums2 = nums2, nums1
        
    m, n = len(nums1), len(nums2)
    left, right, half_len = 0, m, (m + n + 1) // 2
    
    while left <= right:
        partition1 = (left + right) // 2
        partition2 = half_len - partition1
        
        max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        min_right1 = float('inf') if partition1 == m else nums1[partition1]
        
        max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        min_right2 = float('inf') if partition2 == n else nums2[partition2]
        
        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if (m + n) % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
            else:
                return max(max_left1, max_left2)
        
        elif max_left1 > min_right2:
            right = partition1 - 1
        
        else:
            left = partition1 + 1
    
    return -1.0 #Should never reach here


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
        print('\n\tMedian of merged List is: ', findMedianSortedArrays(nums1[i], nums2[i]), sep = '')
        print('-'*100, '\n')
        k += 1


if __name__ == '__main__':
    main()

'''
TC -> O(log(m+n)) because we are effectively cutting the problem size in half at each iteration of the binary search.
SC -> O(1) becaue we're merging the arrays in-place, without using extra space
'''
'''
Leetcode: 4. Median of Two Sorted Arrays.
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/m7Z33JoE51E

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)). !!!! Constriant !!!!

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5

'''
from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m, n = len(nums1), len(nums2)

    i = m - 1
    j = n - 1
    k = m + n - 1
    
    nums1 += [0]*n # Extend nums1 with n zeros elements

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    print('\tMerged Array :', nums1)

    length = n+m
    if length % 2 != 0:
        return nums1[length//2]
    else:
        return (nums1[length//2 - 1] + nums1[length//2]) / 2.0

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
TC -> O(m+n) because we're comparing all the elements in both arrays
SC -> O(1) becaue we're merging the arrays in-place, without using extra space
'''
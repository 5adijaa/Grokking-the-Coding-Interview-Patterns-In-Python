'''
Leetcode: 658. Find K Closest Elements
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/7Xo916nBA6j

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
'''
from typing import List


def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:    
        # 1. We do a BS to find the elts closest to x
        def binary_search(arr, target):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        # 2. and initialize 2 pointers for the sliding window. 
        left = binary_search(arr, x) - 1 
        right = left + 1 #arr=[1,2,3,4,5], x=3, arr[left]=2, arr[right]=4

        # While the sliding window's size is < k
        while right - left - 1 < k :
            if left == -1: #check for out of bounds
                right += 1
                continue
            
            # Expand the window towards the side with the closer number
            # Be careful to not go out of bounds with the pointers
            # |a - num| < |b - num|,
            # |a - num| == |b - num|
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1 #move left backward b/c it's the closest one
            else:
                right += 1 #move right b/c it's the closest one
        
        # Return the window:
        return arr[left+1:right]


def main():

    nums = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 1, 1, 10, 10, 10],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5],
        [1, 2, 4, 5, 6],
        [1, 2, 3, 4, 5, 10]
    ]
    k = [4, 4, 1, 4, 4, 2, 3]
    x = [3, -1, 9, 4, 3, 10, -5]
    for i in range(len(nums)):
        print((i + 1), '.\tThe', k[i],
              'Closest Elements for the number', x[i], 'in the array',
              nums[i], 'are:', findClosestElements(nums[i], k[i], x[i]))
        print('\n', '-' * 100)


if __name__ == '__main__':
    main()

'''
TC -> O(logn + k) because we perform a binary search to find the closest elements to x, and then use a sliding window approach to return k elements. The sliding window approach takes O(k) time because it involves iterating over k elements at most.
SC -> O(1)
'''
'''
Leetcode: 41. First Missing Positive
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/7D36L5ynEDj

Given an unsorted integer array nums, return the smallest missing positive integer.
Constraint: You must implement an algorithm that runs in O(n) time and uses constant extra space.

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
'''

from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    n = len(nums)

    # 1. Do Cyclic sort to sort the array, and put every elt at its corresponding index:
    i = 0
    while i < n:
        c = nums[i] - 1 #correct index
        if c >= 0 and c < n and nums[i] != nums[c]:
            nums[i], nums[c] = nums[c], nums[i] #swap
        else:
            i += 1
    
    print('\tsorted array :', nums)
    
    # 2. Check whether the index is equal to elt in the array
    for i in range(n):
        if nums[i] != i+1 :
            return i+1
    
    return n+1

def main():
    arrays = [
        [1, 2, 0],
        [3, 4, -1, 1],
        [7, 8, 9, 11, 12],
        [1, 2, 3, 4], 
        [-1, 3, 5, 7, 1], 
        [1, 5, 4, 3, 2], 
        [-1 , 0, 2, 1, 4], 
    ]
    for i in range(len(arrays)):
        print(i+1, '.\tThe first missing positive integar in the list ', arrays[i], ' is: ', sep = '')
        print('\tFirst missing Positive is: ', firstMissingPositive(arrays[i]))
        print('-' * 80)

if __name__ == '__main__':
  main()

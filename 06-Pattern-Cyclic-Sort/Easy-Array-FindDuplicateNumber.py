'''
Leetcode: 287. Find the Duplicate Number
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/YVE315zYL4n

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Input: nums = [1,3,4,2,2]
Output: 2

Input: nums = [3,1,3,4,2]
Output: 3
'''
from typing import List


def findDuplicate(nums: List[int]) -> int:
    n = len(nums)

    i=0
    while i < n: #Cyclic Sort:
        c = nums[i]-1 #correct index to swap val to
        if nums[i] != nums[c]:
            nums[i], nums[c] = nums[c], nums[i] #swap
        else:
            i+=1
    
    print('\tSorted nums = ', nums)
    
    for i in range(n): #Find the duplicate val
        if nums[i] != i+1: 
            return nums[i]


def main():
    nums = [
        [1, 3, 4, 2, 2],
        [3, 1, 3, 4, 2],
        [1, 3, 2, 3, 5, 4], 
        [2, 4, 5, 4, 1, 3], 
        [1, 6, 3, 5, 1, 2, 7, 4], 
        [1, 2, 2, 4, 3], 
        [3, 1, 3, 5, 6, 4, 2]
    ]
    for i in range(len(nums)):
        print(i + 1, '.\tnums = ', nums[i], sep='')
        print('\tDuplicate number = ', findDuplicate(nums[i]), sep='')
        print('-' * 75)


if __name__ == '__main__':
    main()

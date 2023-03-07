'''
Leetcode: 27. Remove Element 
~ Similar to 26. Remove Duplicates from Sorted Array

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]

'''
from typing import List

def removeElement(nums: List[int], val: int) -> int:
    i = 0
    next_index = 0

    while i < len(nums):
        if nums[i] != val:
            nums[next_index] = nums[i]
            next_index +=1
        i += 1
    
    return next_index

def main():
    tests = [[[1, 1, 2], 1], [[3,2,2,3], 3], [[0,1,2,2,3,0,4,2], 2] ]
    for test in tests:
        print(removeElement(test[0], test[1]))


main()

'''
TC -> O(n) where n in len(nums)
SC -> O(1) Constant Space
'''
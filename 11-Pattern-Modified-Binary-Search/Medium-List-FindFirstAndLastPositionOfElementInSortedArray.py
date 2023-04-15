'''
Leetcode: 34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Input: nums = [], target = 0 -> Array can be empty
Output: [-1,-1]
'''
from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    res = [-1]*2

    n = len(nums)
    left = 0
    right = n - 1

    # First BS to find the first occurence:
    while left < right:
        mid = (left+right)//2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            right = mid
    
    if left >= n or nums[left] != target:
        return res
    else:
        res[0] = left
    

    # Second BS to find the last occurence:
    right = n - 1
    while left < right:
        mid = (left+right+1)//2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else: 
            left = mid
    
    res[1] = right

    return res


def main():
    nums_list = [
        [5,7,7,8,8,10],
        [5,7,7,8,8,10],
        [],
        [0,1,2,4,5,5,5,6,7],
        [4,6,6,6,7]
    ]
    k_list = [8,7,0,5,9]
    for i in range(len(nums_list)):
        print(i+1, '. \tNums = ', nums_list[i], sep='')
        temp = searchRange(nums_list[i], k_list[i])
        print('\tFirst and Last Position of Element', k_list[i], 'is =', temp)
        print('-'*75)


if __name__ == '__main__':
    main()

'''
TC -> O(logn) where n is the length of nums
SC -> O(1)
'''
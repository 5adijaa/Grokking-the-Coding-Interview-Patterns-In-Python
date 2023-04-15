'''
Leetcode: 33. Search in Rotated Sorted Array
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/qVnp1mWMl1D

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [1], target = 0
Output: -1
'''

from typing import List


def search(nums: List[int], target: int) -> int:
    n = len(nums)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        '''
        We have to check in which portion of the array are we in?
        Then, what's gonna happen as a result? Which part of the array do we have to check based on the comparison conditions?
        '''
        
        # 1. We're in the left portion?
        if nums[left] <= nums[mid]:
            if nums[left] <= target and target < nums[mid]:
                right = mid - 1 #Target is within the sorted first portion of the array
            else:
                left = mid + 1 #Target is within the 2nd right portion
        
        # 2. We're in the right portion?
        else:
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1 #Target is within the second half of the array
            else:
                right = mid - 1 #Target is within the first portion
        
    return -1


def main():
    target_list = [0, 0, 3, 6, 3, 6]
    nums_list = [
        [4,5,6,7,0,1,2],
        [1],
        [6, 7, 1, 2, 3, 4, 5], 
        [6, 7, 1, 2, 3, 4, 5],
        [4, 5, 6, 1, 2, 3], [4, 5, 6, 1, 2, 3]]

    for i in range(len(target_list)):
        print((i + 1), '.\tRotated array: ', nums_list[i], '\n\ttarget', target_list[i], 'found at index ', \
              search(nums_list[i], target_list[i]))
        print('-' * 80)


if __name__ == '__main__':
    main()

'''
TC -> The time complexity of both approaches is O(log(n)) since we divide the array into two halves at each step.
SC -> O(1)
'''
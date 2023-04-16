'''
Leetcode: 81. Search in Rotated Sorted Array II
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/JPMPr7wvRpP

here is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

 
Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
'''
from typing import List


def search(nums: List[int], target: int) -> bool:
    l, r = 0, len(nums) - 1

    while l <= r:
        
        # Shift to remove duplicate elements
        while l < r and nums[l] == nums[l+1]:
            l += 1
        while l < r and nums[r] == nums[r-1]:
            r -= 1

        mid = (l+r)//2

        if nums[mid] == target:
            return True
        
        if nums[l] <= nums[mid]:
            if nums[l] <= target and target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        else:
            if nums[mid] < target and target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1

    return False 


def main():
    target_list = [2, 3, 0, 19, 3, 3, 6]
    nums_list = [
        [2,5,6,0,0,1,2],
        [2,5,6,0,0,1,2],
        [1,0,1,1,1],
        [13,19,57,-13,3,12],
        [1,2,4,5,6,-2,0],
        [4,5,6,7,0,1,2],
        [6,7,1,2,3,4,5], 
    ]

    for i in range(len(target_list)):
        print((i + 1), '.\tRotated Sorted array II: ', nums_list[i], ', Target =', target_list[i])
        is_exist = search(nums_list[i], target_list[i])
        if is_exist:
            print('\tYes, the target was found')
        else:
            print('\tThere is No target in the array')
        print('-' * 80)


if __name__ == '__main__':
    main()

'''
TC -> The time complexity is O(log(n)) since we utilized a BS
SC -> O(1)
'''
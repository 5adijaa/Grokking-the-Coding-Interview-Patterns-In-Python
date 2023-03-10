'''
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Input: nums = [1, 1, 2]
Output: 2, nums = [1, 2 ,_]
Explanation: The first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Input: [3, 3, 3, 7, 10, 10]
Output: 3
Explanation: The first three elements after removing the duplicates will be [3, 7, 10]
'''

from typing import List


def removeDuplicates(nums: List[int]) -> int:
    l = 0
    r = 1
    next_index = 1 #index of next non-duplate item

    while r < len(nums):
        if nums[l] != nums[r]:
            nums[next_index] = nums[r] #before incrementing next_index, update it in array
            next_index += 1
        l+=1
        r+=1
    
    return next_index



def main():
    tests = [[1, 1, 2], [3, 3, 3, 7, 10, 10], [0,0,1,1,1,2,2,3,3,4]]
    for i in tests:
        print(removeDuplicates(i))


main()

'''
TC -> O(n) where n in len(nums)
SC -> O(1) Constant Space
'''
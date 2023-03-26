'''
Leetcode: 268. Missing Number
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/YQN5MzGrp50

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
'''
from typing import List


def missingNumber(nums: List[int]) -> int:
    n = len(nums)
    correct_index = 0
    i = 0
    while i < n: #Sort the array using Cyclic Sort, and match every val with its index
        correct_index = nums[i]
        if nums[i] < n and nums[i] != nums[correct_index] :
            nums[i], nums[correct_index] = nums[correct_index], nums[i]  #swap 
        else:
            i += 1


    for i in range(len(nums)):
        if nums[i] != i: #Check whether the index is equal to elt in the array
            return i

    return n #Case where we go out of for loop with the missing number = len(nums), [0,1]

def main():
    numbers = [
        [3,0,1],
        [9,6,4,2,3,5,7,0,1],
        [0,1],
        [8, 3, 5, 2, 4, 6, 0, 1], 
        [1, 2, 3, 4, 6, 7, 8, 9, 10, 11], 
        [0],
    ]

    i = 1
    for nums in numbers:
        print(i, '.\tnums = ', nums, sep = '')
        print('\n\tMissing number: ', missingNumber(nums), sep = '')
        print('-'*50, '\n', sep = '')
        i+=1

main()

'''
TC -> O(n) where n is the number of elements in the input array
SC -> The algorithm runs in constant space O(1)
'''
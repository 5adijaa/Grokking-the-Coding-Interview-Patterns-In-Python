'''
Leetcode: 448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Input: nums = [1,1]
Output: [2]
'''

from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
        n = len(nums)

        i=0
        while i < n: #Cyclic Sort
            c = nums[i] - 1
            if nums[i] != nums[c]:
                nums[i], nums[c] = nums[c], nums[i]
            else:
                i += 1
        
        print('\tCyclic sort', nums)
        
        res = []
        for i in range(n):
            if nums[i] != i+1:
                res.append(i+1)
        
        return res

def main():
    nums = [
        [4, 3, 2, 7, 8, 2, 3, 1],
        [1, 1], 
        [1, 4, 5, 5, 1, 3], 
        [1, 6, 3, 5, 1, 2, 7, 4], 
        [1, 2, 2, 4, 4], 
    ]
    for i in range(len(nums)):
        print(i + 1, '.\tnums = ', nums[i], sep='')
        print('\tDisappeared numbers = ', findDisappearedNumbers(nums[i]), sep='')
        print('-' * 75)


if __name__ == '__main__':
    main()
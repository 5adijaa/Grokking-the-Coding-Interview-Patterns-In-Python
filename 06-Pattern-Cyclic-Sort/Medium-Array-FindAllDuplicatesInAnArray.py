'''
Leetcode: 442. Find All Duplicates in an Array

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Input: nums = [1,1,2]
Output: [1]
'''
from typing import List


def findDuplicates(nums: List[int]) -> List[int]:
    n = len(nums)

    i=0
    while i < n: #Cyclic Sort
        c = nums[i]-1
        if nums[i] != nums[c]:
            nums[i], nums[c] = nums[c], nums[i] #swap
        else:
            i+=1
    
    print('\tCyclic sort of the list', nums)
        
    res = []
    for i in range(n):
        if nums[i] != i+1:
            res.append(nums[i])
    
    return res
    

def main():
    arrays = [
        [1, 2, 1],
        [4, 3, 2, 7, 8, 2, 3, 1],
        [1, 2, 3, 3, 4, 4], 
        [1, 5, 5, 3, 2], 
    ]
    for i in range(len(arrays)):
        print(i+1, '.\tFind All duplicates in the list ', arrays[i], sep = '')
        print('\tDuplicates = ', findDuplicates(arrays[i]))
        print('-' * 80)

if __name__ == '__main__':
  main()

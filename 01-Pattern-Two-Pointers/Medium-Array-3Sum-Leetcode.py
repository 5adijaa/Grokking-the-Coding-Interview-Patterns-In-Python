'''
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''
from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    triplet = []

    for i, val in enumerate(nums):
        if i>0 and val == nums[i-1]: #skip if we found any duplicate of i
            continue
        
        left = i+1
        right = len(nums) -1
        while left < right:
            three_sum = val + nums[left] + nums[right]
            
            if three_sum == 0:
                triplet.append([val, nums[left], nums[right]])
                left += 1
                # [0,0,0,0] # skip if we found any duplicate of left. right duplicates will be skipped automatically
                while nums[left] == nums[left-1] and left<right:
                    left += 1
            
            elif three_sum < 0 :
                left += 1
            
            else:
                right -= 1
                
    return triplet

def main():
    test_cases = [[-1,0,1,2,-1,-4],[1,-1,0],[-1,2,1,-4,5,-3],[0,1,1],[0,0,0],[0,0,0,0]]
    i=1
    for nums in test_cases:
        print('-'*10, 'Test Case #', i , '-'*10)
        print(threeSum(nums))
        i+=1

if __name__ == '__main__':
    main()

'''
TC-> sorting: O(nlogn) & nested loops: O(n^2) => which will be simplified to O(n^2)
SC-> triplet array O(n/2) & sorting: O(n) => which will be simplified to O(n) 
'''
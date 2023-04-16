'''
Leetcode: 540. Single Element in a Sorted Array
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/3wGGmy0qwqx

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10
'''
from typing import List


def singleNonDuplicate(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left+right)//2

        if mid % 2 != 0: #If mid is odd, decrement it, (useful to check mid & its mid+1, are they =)
            mid -= 1 

        if nums[mid] == nums[mid+1]: #In this case, The single elt must appear after the mid point
            left = mid + 2
        else: #Otherwise we must search before the mid point
            right = mid
    
    return nums[left] 

def main():
    nums = [[1, 1, 2, 3, 3, 4, 4, 8, 8], [3, 3, 7, 7, 10, 11, 11], [1, 2, 2, 3, 3, 4, 4], [1, 1, 2, 2, 3, 4, 4, 5, 5], [1, 1, 2, 3, 3], [1, 1, 2], [1], [0, 2, 2, 3, 3, 4, 4, 5, 5]]

    for i in range(len(nums)):
        print(str(i + 1) + '.\tThe Array = ', nums[i])
        print('\tSingle Element Found: ', singleNonDuplicate(nums[i]))
        print('-' * 100)

if __name__ == '__main__':
    main()

'''
TC -> O(logn) since we conduct a binary search on the elements.
SC -> O(1) because we only use constant space to keep track of where we are in the search.
'''
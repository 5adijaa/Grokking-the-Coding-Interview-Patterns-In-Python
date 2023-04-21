'''
Leetcode: 45. Jump Game II
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/gk5gqlvmwpG

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2
'''

from typing import List


def jump(nums: List[int]) -> int:
    # base case:
    if len(nums) == 1:
        return 0

    jumps = 0 #min number of jumps to reach nums[n-1]
    farthest = 0 #farthest point that can be reached from any given index in the arr.
    curr_end = 0 #tracking the curr end of the curr jump that we can reach in that index

    for i in range(len(nums)-1):
        farthest = max(farthest, i+nums[i]) #i+nums[i] is furthest point that we can reach
        if i == curr_end:
            jumps += 1
            curr_end = farthest
    
    return jumps


def main():
    nums = [
        [2, 3, 1, 1, 4],
        [3, 2, 1, 0, 4],
        [3, 2, 2, 0, 1, 4],
        [3, 2, 1, 0, 4],
        [0],
        [4, 0, 0, 0, 1],
        [3, 3, 3, 3, 3],
        [1, 2, 3, 4, 5, 6, 7]
    ]

    for i in range(len(nums)):
        print(i + 1, '.\tInput array: ', nums[i])
        print('\tThe minimum number of jumps to reach the last index is', jump(nums[i]))
        print('-' * 100)


if __name__ == '__main__':
    main()


'''
TC -> O(n) where n is the length of the arr
SC -> O(1) We don't use any additional data structures
'''
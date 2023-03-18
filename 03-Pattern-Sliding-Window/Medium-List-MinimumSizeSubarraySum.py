'''
leetcode: 209. Minimum Size Subarray Sum
https://www.educative.io/courses/grokking-coding-interview-patterns-python/R1jM9YD1myV

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Input: target = 4, nums = [1,4,4]
Output: 1
'''

from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    window_size = float('inf')
    start = 0
    total_sum = 0
    
    for end in range(len(nums)):
        total_sum += nums[end]
        
        # check if we can remove elements from the start of the subarray
        # while still satisfying the target condition
        while total_sum >= target:
            curr_subarray_size = end - start + 1
            window_size = min(window_size, curr_subarray_size)
            total_sum -= nums[start]
            start += 1

    if window_size == float('inf'):
        return 0
    
    return window_size


def main():
    target = [7, 4, 11, 10, 5, 15]
    input_arr = [[2, 3, 1, 2, 4, 3], [1, 4, 4], [1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 3, 4], [1, 2, 1, 3], [5, 4, 9, 8, 11, 3, 7, 12, 15, 44]]

    for i in range(len(input_arr)):
        window_size = minSubArrayLen(target[i], input_arr[i])
        print(i+1, '.\t min_sub_array_len(',
              target[i], ', ', (input_arr[i]), '): ', window_size, sep='')
        print('-'*72)


if __name__ == '__main__':
    main()

'''
TC -> O(n): As we use a fixed size array and slide a specific size of the window over the whole array, the time complexity of this solution is O(n)
SC -> O(1): because we used a fixed amount of extra space in memory
'''
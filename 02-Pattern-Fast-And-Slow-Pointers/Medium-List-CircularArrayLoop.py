'''
Leetcode: 457. Circular Array Loop
https://www.educative.io/courses/grokking-coding-interview-patterns-python/JEkl4W3G4PD

You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i: (ie. the value at each index represents the number of places to skip forward (if the value is positive) or backward (if the value is negative).)

If nums[i] is positive, move nums[i] steps forward, and
If nums[i] is negative, move nums[i] steps backward.

Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

A cycle in the array consists of a sequence of indices seq of length k where:
 * Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
 * Every nums[seq[j]] is either all positive or all negative.
 * k > 1
Return True if there is a cycle in nums, or False otherwise.

Input: nums = [2, -1, 1, 2, 2]
Output: true
Explanation: We can see the cycle at indices 0 --> 2 --> 3 --> 0 --> ..., and all of its nodes are white (jumping in the same direction).

Input: nums = [-1, -2, -3, -4, -5, 6]
Output: false
Explanation: The only cycle is of size 1, so we return false.

Input: [2, 2, -1, 2]
Output: true
Explanation: The array has a cycle at indices: 1 -> 3 -> 1

'''

from typing import List

def circularArrayLoop(nums: List[int]) -> bool:
    n = len(nums)

    for i in range(n):
        slow, fast = i, i
        is_forward = nums[i] > 0
        
        while True:
            slow = get_next(slow, is_forward, nums)
            fast = get_next(get_next(fast, is_forward, nums), is_forward, nums)
            
            if slow is None or fast is None:
                break
            
            if slow == fast:
                return True
    
    return False

def get_next(idx, direction, nums):
        if idx is None or nums[idx] == 0:
            return None
        
        if (nums[idx] > 0) != direction:
            return None
        
        new_idx = (idx + nums[idx]) % len(nums)
        if new_idx == idx:
            return None
        
        return new_idx

print(circularArrayLoop([-2,1,-1,-2,-2]))

def main():
    tests = (
        [2, -1, 1, 2, 2], #True
        [-1, -2, -3, -4, -5, 6], #False
        [2, 2, -1, 2], #True
        [-2, 1, -1, -2, -2], #False
        [-1, 2], #False
        [-2, -3, -9], #False
        [-5, -4, -3, -2, -1], #True
        [-1, -2, -3, -4, -5] #False
    )
    i=1

    for test in tests:
        print(f'Test {i}:\tCircular array = {test}')
        print(f'\n\tLoop was found = {circularArrayLoop(test)}')
        print('-'*100, '\n')
        i+=1


if __name__ == '__main__':
    main()
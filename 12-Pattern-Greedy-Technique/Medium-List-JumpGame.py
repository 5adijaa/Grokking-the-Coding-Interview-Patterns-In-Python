'''
Leetcode: 55. Jump Game
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/qAqpMr72Gw0

In a single-player jump game, the player starts at one end of a series of squares, with the goal of reaching the last square. 
At each turn, the player can take up to s steps towards the last square, where s is the value of the current square. 
For example, if the value of the current square is 3, the player can take either 3 steps, or 2 steps, or 1 step in the direction of the last square. The player cannot move in the opposite direction, that is, away from the last square. 
You have been tasked with writing a function to validate whether a player can win a given game or not.

You've been provided with the 'nums' integer array, representing the series of squares. The player starts at the first index and, following the rules of the game, tries to reach the last index.

If the player can reach the last index, your function returns TRUE; otherwise, it returns FALSE.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
'''
from typing import List


def canJump(nums: List[int]) -> bool:
    # 1. Set the last element in the array as your initial target.
    target = len(nums) - 1
    
    # 2. Traverse the list from the end
    for i in range(len(nums)-2, -1, -1):
        # 3. If the current index is reachable from any preceding index, 
        # based on the value at that index, make that index the new target.
        if target <= i + nums[i]: #nums[i] represents number of jumps we can make
            target = i
    
    # 4. We are able to move each current target backwards all the way to the first index of the array,
    # => We’ve found a path from the start to the end of the array. Return TRUE
    if target == 0 :
        return True
    
    # 5. We reach the first index without finding any index from which the current target is reachable
    return False

def main():
    nums = [
        [2, 3, 1, 1, 4],
        [3, 2, 1, 0, 4],
        [3, 2, 2, 0, 1, 4],
        [2, 3, 1, 1, 9],
        [3, 2, 1, 0, 4],
        [0],
        [1],
        [4, 3, 2, 1, 0],
        [1, 1, 1, 1, 1],
        [4, 0, 0, 0, 1],
        [3, 3, 3, 3, 3],
        [1, 2, 3, 4, 5, 6, 7]
    ]

    for i in range(len(nums)):
        print(i + 1, '.\tInput array: ', nums[i])
        print('\tCan we reach the very last index? ',
              'Yes.' if canJump(nums[i]) else 'No.',)
        print('-' * 100)


if __name__ == '__main__':
    main()


'''
TC -> O(n) where n is the length of the arr
SC -> O(1) We don't use any additional data structures
'''
'''
Leetcode: 239. Sliding Window Maximum
https://www.educative.io/courses/grokking-coding-interview-patterns-python/RMkpmAllP9L

Given an integer array and a window of size k, find the current maximum value in the window as it slides through the entire array.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Input: nums = [1], k = 1
Output: [1]
'''

from typing import List
from collections import deque

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    window = deque()
    result = []

    # Check if k > len(nums) => then, set k to length of nums
    if k > len(nums):
        k = len(nums)

    # Build the first window out and Find out the first maximum in it
    for i in range(k):
        while window and nums[i] > nums[window[-1]]:
            window.pop()
        window.append(i)
    result.append(nums[window[0]])

    # Traverse to find maximum in remaining windows
    for i in range(k, len(nums)):
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        
        # Remove first index from the window deque if it doesn't fall in the current window anymore
        # -> To pass test case: [1,-1]
        if window and window[0] <= (i-k):
            window.popleft()
        
        window.append(i)
    
        result.append(nums[window[0]])

    return result


def main():
    k_list = [3, 1, 1, 3, 3, 3, 2, 4, 3, 2, 3, 18]
    nums = [
        [1, 3, -1, -3, 5, 3, 6, 7],
        [1, -1],
        [1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67],
        [4, 5, 6, 1, 2, 3],
        [9, 5, 3, 1, 6, 3],
        [2, 4, 6, 8, 10, 12, 14, 16],
        [-1, -1, -2, -4, -6, -7],
        [4, 4, 4, 4, 4, 4]
    ]

    for i in range(len(nums)):
        print(i + 1, ". Original array:\t", nums[i], sep="")
        print("Window size:\t\t", k_list[i])
        print("Max in Sliding Window:\t", maxSlidingWindow(nums[i], k_list[i]))
        print("-"*100)


if __name__ == '__main__':
    main()


'''
TC -> 
To get a clearer understanding of the time complexity of our solution, we need to consider the different ways in which the values in the input list change. The values in the list can be:
 1- Strictly increasing
 2- Strictly decreasing
 3- Constant
 4- Mixed, for example, increasing, decreasing, constant, then decreasing again, then constant, then increasing, then constant and then decreasing

 Let's consider the 1st case, that is, when the values in the array are strictly increasing. The first time the window moves forward, the new element is larger than all the other elements in the deque, so we have to perform the pop() operation k times. Then, in all the subsequent steps, the pop() operation is performed only once O(1), as the deque will only contain one element from this point onwards. The number of subsequent steps is n-k. So, the complexity in this case is: O(k+n-k), that is O(n).

 In the 2nd case, every time the window moves forward, the new element is smaller than all the other elements in the deque, so the popleft() operation is only performed once in every subsequent step, to remove the element which does not fall in the window anymore. So, the time complexity in this case is O(n-k+1), that is: O(n-k).

 In the 3rd case, the same behaviour is repeated as in the second case, so the time complexity is O(n-k) here too.

 Finally, in the 4th case, the time complexity for increasing values as well as decreasing and constant values will be the same as explained above. The only other situation is when the values increase after staying constant, or right after a sequence of decreasing numbers. In either case, we incur a cost of O(k), as we clean up the deque using the pop() operation. If there is an increase in value after every � w elements, we pay the O(k) cost to clean up the deque. This can only happen n/k times. So, the clean-up cost with such data will be O(n - (n/w) + ((n/w)w)), that is: O(n).

 SC -> The space complexity of this solution is O(k), where k is the window size.
'''
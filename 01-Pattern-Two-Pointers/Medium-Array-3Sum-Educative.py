'''
https://www.educative.io/courses/grokking-coding-interview-patterns-python/x150lJ1nOn3

Given an array of integers, nums, and an integer value, target, determine if there are any three integers in nums whose sum equals the target. Return TRUE if three such integers are found in the array. Otherwise, return FALSE.
Input-> nums = [3,7,1,2,8,4,5] target=20
Output-> True (20 is sum of 7+8+5)
'''

from typing import List

def find_sum_of_three(nums: List[int], target: int) -> bool:
    nums.sort()

    # Fix one element at a time and find the other two
    for i in range(len(nums)):
        low = i+1
        high = len(nums)-1
        
        while low < high:
            # Check if the sum of the triple is equal to the sum of target
            sum = nums[i]+nums[low]+nums[high]
            if sum == target:
                return True                
            elif sum < target:
                low +=1
            else:
                high -= 1
            
    return False


def main():
    test_cases = [
        [[1,-1,0],-1],
        [[3,7,1,2,8,4,5],10],
        [[-1,2,1,-4,5,-3],7],
        [[3,7,1,2,8,4,5],20]
    ]
    i=1
    for t_case in test_cases:
        print('-'*10, 'Test Case #', i , '-'*10)
        print(find_sum_of_three(t_case[0], t_case[1]))
        i+=1

if __name__ == '__main__':
    main()

'''
Time Complexity: 
 ** Sorting the array: O(nlog(n))
 ** Nested loop to find the triplet: O(n^2)
=> which can be simplified to O(n^2)

Space Complixity:
=> In python, space complixity of sort() function is O(n)
'''
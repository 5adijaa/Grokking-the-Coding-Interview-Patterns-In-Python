'''
Leetcode: 698. Partition to K Equal Sum Subsets

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Input: nums = [1,2,3,4], k = 3
Output: false

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Decision Tree:
-> We know that we have a target sum to reach that is: target_sum = sum(nums) // k
-> We gonna build our tree decision based on adding an item to the set or not. So, we have 2 choices: either we include the item or we dont add it:
target_sum = 20//4 = 5
                                []
        4                                                         0
    4+3         4                                           0+3         0
     X      4+2         4                                3+2    3    0+2   2
             X      4+3            4                    ....         ....
                     X      4+5            4
                             X       4+2          4
                                      X       4+1   4
                                              =5 
                                            =>we found a target 
                                            down this branch
                                            => [4,1]
                                            => we are not allowed to use these visited items on the next subsets

The height of the tree is = n
The number of decisions (branches) are = 2
=> O(2^n) to build one valid subset
=> the whole Time complexity to find k valid subsets that sum up to k is: O(k*2^n)
'''

from typing import List


def canPartitionKSubsets(nums: List[int], k: int) -> bool: 
    if sum(nums) % k: 
        return False

    nums.sort(reverse=True)        
    
    n = len(nums)
    target_sum = sum(nums) // k
    visited = [False]*n
    
    def backtrack(idx, left_k, curr_subset_sum):
        if left_k == 0: #base case: we built all subsets that sum up to k
            return True
        if curr_subset_sum == target_sum: #we built a subset, now we need to build the next ones
            return backtrack(0, left_k - 1, 0)
        
        for i in range(idx, n):
            # For each item (nums[i]) we have 2 choices: either choose it or not
            # Plus, we only choose it if it's not visited yet or it < target_sum
            if visited[i] or curr_subset_sum + nums[i] > target_sum:
                continue
            if i > 0 and not visited[i-1] and nums[i] == nums[i-1]: #Skip duplicates
                continue
            visited[i] = True
            if backtrack(i+1, left_k, curr_subset_sum + nums[i]):
                return True
            visited[i] = False
            if curr_subset_sum == 0: #break null branch
                break
    
        return False
    
    return backtrack(0,k,0)

def main():
    nums = [
        [4,3,2,3,5,2,1],
        [1,2,3,4],
        [1,1,1,1,2,2,2,2],
        [2,2,2,2,3,4,5],
        [1,1,1,1,2,2,2,2],
        [4,2,9,8,1,1,5,9,4,3,5,6,3,5,7],
        [1,1,2,4]
    ]
    k_values = [4,3,2,4,4,9,4]

    for i in range(len(nums)):
        print(f'Does nums = {nums[i]}, has k = {k_values[i]} non-empty subsets whose sums are all equal?')
        is_partition = canPartitionKSubsets(nums[i], k_values[i])
        if is_partition:
            print('\t => Yes')
        else:
            print('\t => No,')

main()
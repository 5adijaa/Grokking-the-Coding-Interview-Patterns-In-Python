'''
Find K-Sum Subsets: (Educative) https://www.educative.io/courses/grokking-coding-interview-patterns-python/m7R4VYVPDE0

Given a set of n positive integers, find all the possible subsets of integers that sum up to a number k.

Constraints:
* 1 ≤ n ≤ 10
* 1 ≤ x ≤ 100, where x is any member of the input set
* 1 ≤ k ≤ 10^3

Input: [1, 3, 5, 21, 19, 7, 2], k=10
Output: [[3,7], [3,5,2], [1,7,2]]

Input: [3, 34, 4, 12, 5, 2], k=9
Output: [[4, 5]]

Instructions:
* Find all possible subsets
* Find the sum of the elements of each subset
* if the sum of any subset = k => then add this subset to the result list.
'''

from typing import List

def get_bit(num, bit):
    tmp = num & (1 << bit)
    if tmp == 0: return 0
    else:
        return 1


def getKSumSubsets(nums: List[int], target_sum) -> List[List[int]]:
    subsets = []
    n = len(nums)
    subsets_count = 2**n #the size of all subsets that can be formed (2^n)
    
    for i in range(subsets_count):
        st_sum = 0
        st = set()
        for j in range(0, n):
            if get_bit(i, j) == 1 and nums[j] not in st:
                st.add(nums[j]) 
        
        for s in st:
            st_sum += s

        if st_sum == target_sum:
            subsets.append(list(st))

    return subsets


def main():
    inputs = [
        [1, 3, 5, 21, 19, 7, 2], 
        [3, 34, 4, 12, 5, 2], 
        [8,13,3,22,17,39,87,45,36], 
        [8,13,3,22,17,39,87,45,36]
    ]
    targets = [10, 9, 3, 135]

    for i in range(len(inputs)):
        print(i + 1, '. Set: ', inputs[i], sep='')
        subsets = getKSumSubsets(inputs[i], targets[i])
        print(f'\n\tThe possible subsets that sum up to k={targets[i]}:', subsets)
        print('-'*100)


if __name__ == '__main__':
    main()

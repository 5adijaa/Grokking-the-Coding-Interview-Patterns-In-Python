'''
Leetcode: 78. Subsets
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/q25BJG18g6y

Given an integer array nums of unique elements, return all possible 
subsets (A subset of an array is a selection of elements (possibly none) of the array.)

All the numbers of array are unique.

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]
'''

from typing import List

def get_bit(num, bit):
    tmp = num & (1 << bit)
    if tmp == 0: return 0
    else:
        return 1


def findAllSubsets(nums: List[int]) -> List[List[int]]:
    subsets = []
    n = len(nums)

    if not nums:
        return [[]]
    else:
        subsets_count = 2**n #the size of the subsets to be constructed (2^n)
        for i in range(subsets_count):
            st = set()
            for j in range(0, n):
                if get_bit(i, j) == 1 and nums[j] not in st:
                    st.add(nums[j])  

            subsets.append(list(st))

        return subsets


def main():
    inputs = [[1, 2, 3], [], [2, 5, 7], [1, 2], [7, 3, 1, 5]]

    for i in range(len(inputs)):
        print(i + 1, '. Set:     ', inputs[i], sep='')
        subsets = findAllSubsets(inputs[i])
        print("\n   Subsets:", subsets)
        print('-'*100)


if __name__ == '__main__':
    main()

'''
TC -> Time complexity of this solution is exponential, O(2^n*n) where n is the number of integers in the given list.
SC -> O(2^n) n is the number of integers in the given list.
'''
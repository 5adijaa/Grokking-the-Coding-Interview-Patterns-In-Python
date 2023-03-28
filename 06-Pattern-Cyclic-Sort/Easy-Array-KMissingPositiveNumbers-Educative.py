'''
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/YQvE1E4y0RO

For a given unsorted array, find the first k missing positive numbers in that array.

Constraints:
- Ignore all negative numbers.
- If missing_nums.length ≠k, add missing numbers up to k
- 1 ≤ k ≤ 10^4 
- 1 ≤ missing_nums.length ≤ 200

Input: [3, -1, 8, 2, 5], k=4
Output: [1,4,6,7]
Explanation: The first 4 missing positive numbers are: 1, 4, 6, 7

Input: array = [1, 2, 3, 0, 4, 9, 7], k=4
Output: 

Input: [2, 3, 4], k=3
Output: [1, 5, 6]
Explanation: The 3 first missing positive numbers are 1, 5 and 6.
'''

from typing import List


def firstKMissingNumbers(arr: List[int], k: int) -> List[int]:
    n = len(arr)
    i=0
    while i < n: #Cyclic Sort
        c = arr[i]-1
        if c < n and c >= 0 and arr[i] != arr[c]:
            arr[i], arr[c] = arr[c], arr[i]
        else:
            i+=1
    
    missing_numbers = []
    count = 0
    for i in range(n): #add missing numbers that are less than n to 'res' arr
        if arr[i] != i+1:
            count += 1
            missing_numbers.append(i+1)
            if count == k:
                return missing_numbers
        
    i = n
    while count < k: #remaining missing numbers that are higher than n
        if i+1 not in missing_numbers:
            count += 1
            curr_missing = i+1
            missing_numbers.append(curr_missing)
            if count == k:
                return missing_numbers
        i += 1    


def main():
    arrays = [
        [3,-1,8,2,5],
        [1,2,3,0,4,9,7],
        [2,3,4],
        [1,2,3,4,5],
        [1,-1,2],
        [-4,6], 
        [0,-5,1,3,5,4],
        [1,-1,-3,8],
        [-23,-4,-1,-54,-6,-9]
    ]
    k = [4,4,3,6,2,4,3,4,3]

    for i, arr in enumerate(arrays):
        print(i+1, '.\tarr = ', arr, sep = '')
        print('\n\tkth Missing Positive Number: ', firstKMissingNumbers(arr, k[i]), sep = '')
        print('-'*55, '\n', sep = '')
    

main()

'''
TC -> O(n), where n is the number of 
SC -> O(k) where k is the number of the missing numbers to be returned.
'''
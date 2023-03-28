'''
Leetcode: 1539. Kth Missing Positive Number

Given an array 'arr' of positive integers sorted in a strictly increasing order, and an integer k.
Return the kth positive integer that is missing from this array.

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

Remark: Since the array is sorted, so we can use binary Search to solve this problem. But Iprefer to go with the Cyclic sort pattern.
'''

from typing import List


def findKthPositive(arr: List[int], k: int) -> int:
    n = len(arr)

    i = 0
    while i < n: #Cyclic Sort, and put every elt at its correspondant index
        c = arr[i]-1
        if c < n and arr[i] != arr[c]:
            arr[i], arr[c] = arr[c], arr[i]
        else:
            i += 1
    
    i = 0
    count = 0
    curr_missing = None
    extra_nums = []
    for i in range(n): #k-th missing number is less than n
        if arr[i] != i+1:
            count +=1
            curr_missing = i+1 #current missing number
            if count == k:
                return curr_missing
        if arr[i] > n: #put the elts that are not in their right index in extra_nums array
            extra_nums.append(arr[i])
        
    i = n
    while True: #k-th missing number is higher than n
        if i+1 not in extra_nums:
            count += 1
            curr_missing = i+1
            if count == k:
                return curr_missing
        i += 1


def main():
    arrays = [
        [1,2,3,5],
        [2,3,4,7,11],
        [1,2,3,4],
        [0,1],
        [1, 2, 3, 4, 6, 7, 8, 9, 10, 11], 
        [0],
        [5,6,7,8],
    ]

    k = [1,5,2,2,3,1,1]

    for i, arr in enumerate(arrays):
        print(i+1, '.\tarr = ', arr, sep = '')
        print(f'\n\t{k[i]}-th Missing Positive Number: ', findKthPositive(arr, k[i]), sep = '')
        print('-'*50, '\n', sep = '')

main()

'''
TC -> O(n) where n is the number of elements in the input array
SC -> O(k) because we used ans extra_nums array to store the extra elements that are not in their correct index with k<=n
'''
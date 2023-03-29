'''
Leetcode: 765. Couples Holding Hands

There are n couples sitting in 2n seats arranged in a row and want to hold hands.

The people and seats are represented by an integer array row where row[i] is the ID of the person sitting in the ith seat. The couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2n - 2, 2n - 1).

Return the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

Input: row = [0,2,1,3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.

Input: row = [3,2,0,1]
Output: 0
Explanation: All couples are already seated side by side.
'''

from typing import List


def minSwapsCouples(row: List[int]) -> int:
    n = len(row)
    min_swaps = 0

    i = 0
    while i < n: #Cyclic Sort            
        # Case where we encounter an even number like 2 or 0
        # next number can form a pair if it is equal after adding 1 from this number (0,1)
        if row[i] % 2 == 0 and row[i+1] != row[i] + 1:
            c = row.index(row[i]+1) #Get correct index to swap with
            row[i+1], row[c] = row[c], row[i+1]
            min_swaps += 1
        
        # Case where we encounter an odd number like 3
        # next number can form a pair if it is equal after subtracting 1 from this number (3,2)
        elif row[i] % 2 != 0 and row[i+1] != row[i] - 1:
            c = row.index(row[i]-1)
            row[i+1], row[c] = row[c], row[i+1]
            min_swaps += 1
        else:
            i += 2 #couples are combined as pair, so we check in every even index positions (0,2,4,6,..)
    
    print('\tswaped Row:', row)
    
    return min_swaps


def main():
    rows = [
        [0,2,1,3],
        [3,2,0,1],
        [2,0,5,4,3,1],
        [5,0,4,1,3,2],
        [0,4,1,3,5,2]
    ]

    for i in range(len(rows)):
        print(i+1, '.\tRow = ', rows[i], ' is: ', sep = '')
        print('\tMinimun swaps: ', minSwapsCouples(rows[i]))
        print('-' * 80)

if __name__ == '__main__':
    main()

'''
TC -> O(n/2), where n is the number of couples, and we only loop and check every even position 0,2,4, etc because the couples are numbered in order: (0,1), (2,3), (4,5) etc
SC -> O(1) no extra space needed
'''
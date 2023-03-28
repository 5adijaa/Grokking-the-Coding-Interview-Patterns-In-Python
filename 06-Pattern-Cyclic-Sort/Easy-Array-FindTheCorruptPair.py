'''
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/m2YP8PvNYY9

Given a non-empty unsorted en from a range of 1 to n. Due to some data error, one of the numbers is duplicated, which results in another number missing. Create a function that returns the corrupt pair (missing, duplicated).

Constraints: 1≤ n ≤10^3 and 0 ≤ nums[i] ≤n, where nums is the input put: [4, 1, 2, 1, 6, 3]
Output: (5,1)
Explanation: The missing number is 5 and the duplicate number is 1

Input: [3, 1, 2, 5, 2]
Output: (4,2)
Explanation: The missing number is 4 and the duplicate number is 1
'''
def findCorruptPair(nums):
    n = len(nums)

    i=0
    while i < n: #Cyclic Sort
        c = nums[i]-1
        if c < n and nums[i] != nums[c]:
            nums[i], nums[c] = nums[c], nums[i]  #swap 
        else:
            i += 1
    
    missing = None
    duplicated = None
    for i in range(len(nums)): #Finding the corrupt pair(missing, duplicated)
        if nums[i] != i+1:
            missing = i + 1
            duplicated = nums[i]
    return missing, duplicated


def main():
    arrays = [
        [3, 1, 2, 5, 2],
        [3, 1, 2, 3, 6, 4],
        [4, 1, 2, 1, 6, 3],
        [4, 3, 4, 5, 1],
        [5, 3, 5, 6, 2, 1],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4]
    ]
    for i in range(len(arrays)):
        print(i + 1,  '.\tGiven array: ', arrays[i], sep='')
        result = findCorruptPair(arrays[i])

        if result[0]:
            print('\n\tCorrupt pair: (', result[0], ', ', result[1], ')', sep='')
        else:
            print('\n\tNo corrupt pair found.')
        print('-'*100)


if __name__ == '__main__':
    main()
       
'''
TC -> O(n) because we used the cyclic sort, where n is the size of the n the worst case, let's assume that every element is placed at the wrong index. With every swap operation, there is at least one element that is placed in the right place. The total number of swap operations that need to be performed is O(n). After loop while i < len(nums): is executed, we would've performed exactly n iterations and at most n swaps so the total time complexity would be O(2n) or O(n).
SC -> O(1) because no extra space is used.
'''

'''
leetcode: 56. Merge Intervals
https://www.educative.io/courses/grokking-coding-interview-patterns-python/RLQVvyjr0gR

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3], [2,6], [8,10], [15,18]]
Output: [[1,6], [8,10], [15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Input: intervals = [[1,4], [4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Instructions for the answer with the interviewer ->
1 2 3 4 5 6 7 8   10   15   18
[---]
  [-------]
              [----] 
                       [------]
- should I consider the list as it is sorted or I have to sort it first?
- does the 2nd interval overlap with the previous one?
- if yes: we merge them
    * [1,3] and [2, 6] overlap .. 3>2 => the end of interval  second val 6
- if no: we do nothing, we just add the interval into output list
'''

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()

    output = [intervals[0]]

    for i in range(1, len(intervals)):
        # we want to compare the last interval added to the output list, and the curr one at intervals list.
        last_added_interval = output[-1]
        curr_start = intervals[i][0]
        curr_end = intervals[i][1]

        if last_added_interval[1] >= curr_start:
            last_added_interval[1] = max(last_added_interval[1], curr_end)
        else:
            output.append(intervals[i])
    
    return output

def main():
    v1 = [[1, 5], [3, 7], [4, 6]]
    v2 = [[1, 5], [4, 6], [6, 8], [11, 5]]
    v3 = [[3, 7], [6, 8], [10, 2], [11, 5]]
    v4 = [[1, 5]]
    v6 = [[1, 9], [3, 8], [4, 4]]
    v7 = [[1, 2], [3, 4], [8, 8]]
    v8 = [[1, 5], [1, 3]]
    v9 = [[1, 5], [6, 9]]
    v10 = [[0, 0], [1, 1], [1, 3]]
    v11 = [[1,4],[0,0]]

    v_list = [v1, v2, v3, v4, v6, v7, v8, v9, v10, v11]

    for i in range(len(v_list)):
        print(i + 1, '. Intervals to merge: ', v_list[i], sep='')
        # result = merge(v_list[i])
        print(' Merged intervals:\t', merge(v_list[i]))
        print('-'*65)

if __name__ == '__main__':
    main()


'''
TC -> O(nlog) because we do sort befor looping through the list
SC -> O(n)
'''
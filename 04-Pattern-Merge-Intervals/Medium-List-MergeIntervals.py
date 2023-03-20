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
'''

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  #by default, the interval is closed 

    def set_closed(self, closed):
        ''' set the flag for closed/open '''
        self.closed = closed

    def __str__(self):
        return '[' + str(self.start) + ', ' + str(self.end) + ']' \
            if self.closed else \
                '(' + str(self.start) + ', ' + str(self.end) + ')'

def mergeIntervals(v):
    output = []
    output.append(Interval(v[0].start, v[0].end)) #add the 1st interval to the output list
    for i in range(1, len(v)):
        last_added_interval = output[-1]
        prev_end = last_added_interval.end
        curr_start = v[i].start
        curr_end = v[i].end
        if prev_end >= curr_start:
            last_added_interval.end = max(prev_end, curr_end)
        else:
            output.append(Interval(curr_start, curr_end))
    return output

def interval_list_to_str(lst):
    result_str = ''
    for i in range(len(lst)):
        result_str += str(lst[i]) + ', '
    return '[' + result_str[:-2] + ']'

def main():
    v1 = [Interval(1, 5), Interval(3, 7), Interval(4, 6)]
    v2 = [Interval(1, 5), Interval(4, 6), Interval(6, 8), Interval(11, 15)]
    v3 = [Interval(3, 7), Interval(6, 8), Interval(10, 12), Interval(11, 15)]
    v4 = [Interval(1, 5)]
    v6 = [Interval(1, 9), Interval(3, 8), Interval(4, 4)]
    v7 = [Interval(1, 2), Interval(3, 4), Interval(8, 8)]
    v8 = [Interval(1, 5), Interval(1, 3)]
    v9 = [Interval(1, 5), Interval(6, 9)]
    v10 = [Interval(0, 0), Interval(1, 18), Interval(1, 3)]

    v_list = [v1, v2, v3, v4, v6, v7, v8, v9, v10]

    for i in range(len(v_list)):
        print(i + 1, '. Intervals to merge: ', interval_list_to_str(v_list[i]), sep='')
        result = mergeIntervals(v_list[i])
        print('   Merged intervals:\t', interval_list_to_str(result))
        print('-'*65)

if __name__ == '__main__':
    main()

'''
TC -> O(n) where n is the total number of all intervals in the input list
SC -> O(n) because we need to return an output list of all the merged intervals 
'''
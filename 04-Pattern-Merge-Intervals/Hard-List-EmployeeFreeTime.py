'''
leetcode: 759. Employee Free Time (premium)
https://www.educative.io/courses/grokking-coding-interview-patterns-python/JE0NVAEPo5J

You're given a list 'schedule' of multiple employees, which represents the working time for each employee. Each employee has a list of non-overlapping intervals in sorted order. 

Return the list of finite intervals representing common, positive-length free time for al employees, also in sorted order

Input: Employee Working Hours=[[[2, 3], [7, 9]], [[1, 4], [6, 7]]]
Output: [4,6]
Explanation: All employess are free between [4,6].

Input: Employee Working Hours=[[[1,2], [5,6]], [[1,3]], [[4,10]]]
Output: [3,4]
Explanation: all the employess are free between [3,4].

Input: Employee Working Hours=[[[1,3], [6,7]], [[2,4]], [[2,5], [9,12]]]
Output: [5,6], [7,9]
Explanation: All employess are free between [5,6] and [7,9].

Way to Answer ->
1  2  3  4  5  6  7  9   12
[-----]        [--]        
   [-----]
   [--------]        [----]
            [##]  [##]
** Add all the employee schedules to a new list, then sort it based on its starting time
** Iterate over the new list, and keep track of the previous latest ending time.
** If the starting time for any period occurs after the previous latest ending time. So, => we found a free time interval for all employees and we can add it to the result list.
** Repeat the steps to track the latest ending time and compare with the new starting time to collect all common free intervals in the result list.
'''

# Definition for an Interval
class Interval:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed
    
    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return '[' + str(self.start) + ', ' + str(self.end) + ']' \
            if self.closed else \
                '(' + str(self.start) + ', ' + str(self.end) + ')'
    

def employeesFreeTime(schedule: '[[Interval]]') -> '[Interval]':
    intervals = []
    res = []

    for s in schedule:
        intervals.extend(s)
    
    intervals.sort(key=lambda x: x.start)

    for i in range(1, len(intervals)):
       if intervals[i-1].end < intervals[i].start:
           res.append(Interval(intervals[i-1].end, intervals[i].start))
    
    return res


# Function for displaying interval list
def display(vec):
    string = '['
    if vec:
        for i in range(len(vec)):
            string += str(vec[i])
            if i + 1 < len(vec):
                string += ', '
    string += ']'
    return string

# Driver code:
def main():
    intervals = [
        [[Interval(2, 3), Interval(7, 9)], [Interval(1, 4), Interval(6, 7)]],
        [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]],
        [[Interval(1, 3), Interval(6, 7)], [Interval(2, 4)], [Interval(2, 5), Interval(9, 12)]],
        [[Interval(3, 5), Interval(8, 10)], [Interval(4, 6), Interval(9, 12)], [Interval(5, 6), Interval(8, 10)]],
        [[Interval(1, 3), Interval(6, 9), Interval(10, 11)], [Interval(3, 4), Interval(7, 12)], [Interval(1, 3), Interval(7, 10)], [Interval(1, 4)], [Interval(7, 10), Interval(11, 12)]],
        [[Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8)], [Interval(2, 3), Interval(4, 5), Interval(6, 8)]],
        [[Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)], [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)], [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)], [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)]]

    ]
    i = 1
    for schedule in intervals:
        print(i, '.\tEmployee Schedules:', sep='')
        for s in schedule:
            print('\t\t', display(s), sep='')
        print('\tEmployees\' free time', display(employeesFreeTime(schedule)))
        print('-'*75)
        i += 1


if __name__ == '__main__':
    main()
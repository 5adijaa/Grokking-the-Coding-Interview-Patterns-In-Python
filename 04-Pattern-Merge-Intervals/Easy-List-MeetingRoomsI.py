'''
leetcode: 920. Meeting Rooms

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: (0,30), (5,10) and (0,30),(15,20) will conflict

Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: Two times will not conflict 

Answer Instructions:
5   8  9   15
[---]  [----] No overlap => can attend all meetings
prev_end = 8 .. curr_start= 9 .. 8 < 9 => no overlap .. increment
                                        else if overlap, return False
'''

def canAttendMeetings(intervals) -> bool:
    prev_end = intervals[0][1]

    i=1
    while i < len(intervals):
        curr_start = intervals[i][0]
        if prev_end < curr_start:
            prev_end = intervals[i][1]
            i+=1
        else:
            return False
    
    return True

print(canAttendMeetings([(0,30),(5,10),(15,20)]))
print(canAttendMeetings([(5,8),(9,15)]))
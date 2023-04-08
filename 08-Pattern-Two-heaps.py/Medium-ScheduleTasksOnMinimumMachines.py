'''
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/m79XY1L9QxA

Given a set of n number of tasks, implement a task scheduler method, tasks(), to run in O(n logn) time that finds the minimum number of machines required to complete these n tasks.

input: [(1,7), (8,9), (3,6), (9,14), (6,7)]
output: 2, is the optimal machine required
Explanation: machine1: [(1,7), (8,9)] , machine2: [(3,6), (6,7), (9,14)]

input: T = [(1,5), (8,13), (5,6), (10,14), (6,7)]
output: 2, is the optimal machine required
Explanation: only 2 machines are required to execute all input tasks

input: T = [(2,5), (2,5), (2,5), (2,5), (5,6)]
output: 4, is the optimal machine required

Rq: I only use one min-heap -> similar to leetcode: 919. Meeting Rooms II solution.
'''
import heapq

def tasks(tasks_list):
    tasks_list.sort(key=lambda x:x[0])

    min_machines = 0
    minheap = [tasks_list[0][1]]
    for i in range(1, len(tasks_list)):
        if minheap[0] <= tasks_list[i][0]: #A task was ended, and a machine is available
            heapq.heappop(minheap)
        heapq.heappush(minheap, tasks_list[i][1])
        min_machines = max(min_machines, len(minheap))
    
    return min_machines

def main():
    # each task has a start time and a finish time
    input_tasks_list = [
        [(1,7), (8,9), (3,6), (9,14), (6,7)],
        [(1,5), (8,13), (5,6), (10,14), (6,7)],
        [(2,5), (2,5), (2,5), (2,5), (5,6)],
        [(1, 1), (5, 5), (8, 8), (4, 4), (6, 6), (10, 10), (7, 7)],
        [(1, 7), (1, 7), (1, 7),
        (1, 7), (1, 7), (1, 7)],
        [(1, 7), (8, 13), (5, 6), (10, 14), (6, 7)],
        [(1, 3), (3, 5), (5, 9), (9, 12),
        (12, 13), (13, 16), (16, 17)],
        [(12, 13), (13, 15), (17, 20),
        (13, 14), (19, 21), (18, 20)]
    ]

    # loop to execute till the length of tasks
    for i in range(len(input_tasks_list)):
        print(i + 1, '.\t Tasks = ', input_tasks_list[i], sep='')

        # Output: A non-conflicting schedule of tasks in
        # 'tasks_list' using the minimum number of machines
        print('\t Optimal number of machines = ',
              tasks(input_tasks_list[i]), sep='')
        print('-' * 100)


if __name__ == '__main__':
    main()


'''
TC -> The time complexity of is O(nlogn), where n is the length of the input list. This is because the function first sorts the input list, which takes O(nlogn) time. Then, it iterates through the sorted list and performs heap operations, which take O(logn) time each. The heap operations are performed n times, so the total time complexity of the function is O(nlogn).
The built-in Python functions used in the code are:
- sort(): has O(nlogn) TC, where n is the length of the list.
- heappop() & heappush(): has O(logn), where n is the length of the heap.

SC -> The space complixity is O(n), where n is the length of the input list. This is because this algorithm uses a minheap to keep track of the machines currently in use, and the size of the minheap can be at most n. 
- The sort function has a space complexity of O(logn), where n is the length of the input list. 
- The space complexity of the built-in Python functions heappop and heappush are O(1).

'''
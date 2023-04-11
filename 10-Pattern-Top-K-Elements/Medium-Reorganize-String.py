'''
Leetcode: 767. Reorganize String
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/mypRB5R8393

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return '' if not possible.

Constraints:
- 1 <= s.length <= 500
- s consists of lowercase English letters.

Input: s = 'aab'
Output: 'aba'

Input: s = 'aaab'
Output: ''

Input: s = 'aaabc'
Output: 'abaca'
'''
from collections import Counter
from heapq import *

def reorganizeString(s: str) -> str:
    mapping = Counter(s) #Store each char and its frequency in a hashmap 'mapping'

    max_heap = []
    for c in mapping:
        heappush(max_heap, (-mapping[c], c))

    prev = None #temporary variable to store prev char that we popped & has count!=0
    res = ''
    while max_heap or prev:
        if not max_heap and prev: #heap is now empty but we still have adjacents
            return ''
        
        count, char = heappop(max_heap)
        res += char
        count += 1 #decrement count (in python max_heap is stored with minus '-')

        if prev: #check to push the char back to the heap
            heappush(max_heap, prev)
            prev = None
        
        # But before pushing it back to the heap, we have to set it to the most prev used char that have count>0, to avoid adjacency values
        if count != 0:
            prev = (count, char)
    
    return res
    
def main():
    test_cases = ['aaabc', 'programming', 'fofjjb', 'abbacdde', 'aba', 'awesome', 'aaab']
    for i in range(len(test_cases)):
        print(i+1, '. \tInput string is: "', test_cases[i], '"', sep='')
        temp = reorganizeString(test_cases[i])
        print('\tReorganized string: "', temp + '' if temp else '"', sep='')
        print('-'*60)


if __name__ == '__main__':
    main()

'''
TC -> 
The time complexity of this function is O(n log n), where n is the length of the input string. This is because the function first iterates over the input string to create a hashmap, which takes O(n) time. Then, it constructs a max-heap using the character frequency data, which takes O(n log n) time. Finally, it iterates over the heap and in each iteration, it pops the most frequently occurring character, which takes O(log n) time, and appends it to the result string. The while loop runs for n iterations, so the total time complexity is O(n log n).
RQ:
The built-in Python functions invoked by the code are:
- hashmap.get(c,0): O(1)
- heappush(max_heap, (-hashmap[c], c)): O(log n)
- heappop(max_heap): O(log n)
- heappush(max_heap, prev): O(log n)
SC ->
he space complexity is O(n), where n is the length of the input string. This is because we are using a hashmap to store the frequency of each character in the input string, which takes up O(n) space. We are also using a max heap to store the character frequency data, which takes up O(n) space. The result string res also takes up O(n) space. Therefore, the total space complexity of the function is O(n).
'''
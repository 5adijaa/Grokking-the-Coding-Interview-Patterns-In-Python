'''
Leetcode: 3. Longest Sub_string Without Repeating Characters
https://www.educative.io/courses/grokking-coding-interview-patterns-python/N04EM6lMvk2

Problem:
Given a string s, find the length of the longest sub_string without repeating characters.

Input: s = 'abcabcbb'
Output: 3
Explanation: The answer is 'abc', with the length of 3.

Input: s = 'bbbbb'
Output: 1
Explanation: The answer is 'b', with the length of 1.
'''

def lengthOfLongestSubstring(s: str) -> int:   
        sub_string = set()
        max_length = 0

        l = 0
        r = 0

        while r < len(s):
            while s[r] in sub_string:
                sub_string.remove(s[l])
                l += 1
            sub_string.add(s[r])
            max_length = max(max_length , r-l+1)
            r += 1 
        
        return max_length


def main():
    strings = [ 'abcabcbb', 'pwwkew', 'bbbbb', 'ababababa', '', 'ABCDEFGHI', 'ABCDEDCBA',
        'AAAABBBBCCCCDDDD']
    
    for i in range(len(strings)):
        print(i + 1, '. \t Input String: ', strings[i], sep='')
        print('\t Length of longest substring: ',
                (lengthOfLongestSubstring(strings[i])))
        print('-' * 55)


if __name__ == '__main__':
    main()

'''
TC -> O(n) because we have to iterate over all the n elements in the string. 
SC -> O(n) because we needed am extra space to store the last occurrence of each element. In the worst-case scenario, all of the elements can be unique and we need to store all n elements. Therefore, the space complexity will be O(n).
'''
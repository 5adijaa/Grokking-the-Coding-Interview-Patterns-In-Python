'''
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/YQOnN622WRO
Leetcode: 151. Reverse Words in a String

Given an input string s, reverse the order of the words
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
'''

def reverseWords(s: str) -> str:
    lst = s.split()

    start, end = 0, len(lst)-1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    
    return ' '.join(lst)

def main():
    string_to_reverse = ['  Hello World!   ','All    Together', 'the  sky is blue']

    for i in range(len(string_to_reverse)):
        print('Reversed string:\t', reverseWords(string_to_reverse[i]))
        print('-'*50)


if __name__ == '__main__':
    main()

'''
TC -> split function: O(n), While loop: O(n) and join function: O(n) => O(3n) ~ O(n)
SC -> we split the string into a list of words => O(n)
'''
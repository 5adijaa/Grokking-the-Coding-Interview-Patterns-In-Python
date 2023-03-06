'''
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/YQOnN622WRO
Leetcode: 151. Reverse Words in a String

Given an input string s, reverse the order of the words
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
'''

# Two pointers : 'start' and 'end'
# Start with both of them from the end of the string,
# There are 2 possibilities: weither 'start' and 'end' will point on a space or on a chararcter
# -> decrement both 'end' and 'start' to skip trailing spaces, 
# -> otherwise, let 'end' where is it, and decrement 'start' until a space was found and this mark a word => put it on our output string 
# once the 'start' reaches the beginning. We have 2 possibilities : weither 'start' will point on the first word or on leading space(s)
# -> Add the first word, in this case end>=0
# -> otherwise, trim the leading space(s), in this case end<= 0
def reverseWords(s: str) -> str:
    start = len(s) - 1
    end = len(s) - 1
    output = ''

    # while start > 0 :
    for start in range(len(s)-1, -1, -1):
        c = s[start]
        if c == ' ':
            if start == end :
                # start -= 1
                end -= 1
            else:
                output += s[start+1: end+1] + ' '
                end = start - 1
                # start -= 1
        # else:
        #     start -= 1
    
    if end >= 0 :
        output += s[: end+1]
    else:
        output = output[:-1]
    
    return output

def main():
    string_to_reverse = ['  Hello World!   ', ' asdasd df f', 'All    Together', 'the  sky is blue']

    for i in range(len(string_to_reverse)):
        print('Pur string: ', '"', string_to_reverse[i], '"')
        print('\n')
        print('Reversed string: ', '"', reverseWords(string_to_reverse[i]), '"', sep='')
        print('-'*50)


if __name__ == '__main__':
    main()

'''
TC -> O(n)
SC -> O(1)
'''
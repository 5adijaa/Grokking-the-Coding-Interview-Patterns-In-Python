'''
https://leetcode.com/problems/valid-palindrome/
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

# Check if a character is alphanumeric
def is_alpha_num(char: str) -> bool:
    return (ord('a') <= ord(char) <= ord('z')) or (ord('A') <= ord(char) <= ord('Z')) or (ord('0') <= ord(char) <= ord('9'))

def is_palindrome(s: str) -> bool:
    # base case
    if s == '' or s == ' ' or len(s) == 1:
        return True
    
    l = 0
    r = len(s)-1

    while l < r:
        if not is_alpha_num(s[l]):
            l += 1
        elif not is_alpha_num(s[r]):
            r -= 1
        elif s[l].lower() != s[r].lower():
                return False
        else:
            l, r = l + 1, r - 1
    return True


def main():
    test_cases = ['A man, a plan, a canal: Panama', 'race a car', ' ', 'kay1yak']
    i=1
    for s in test_cases:
        print('-'*10, 'Test Case #', i , '-'*10)
        print(is_palindrome(s))
        i+=1

if __name__ == '__main__':
    main()

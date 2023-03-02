'''
Write a function that takes a string s as input and checks whether it's a palindrome or not.
'''

def is_palindrome(s: str) -> bool:
    l = 0
    r = len(s)-1

    while(l<r):
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    
    return True

def main():
    test_cases = ['kayak', 'RACEACAR', 'ABCDEFGFEDCBA', 'ABCBA', 'ABBA', 'RACEACAR']
    for i in range(len(test_cases)):
        print("Test Case #", i + 1)
        print(is_palindrome(test_cases[i]))
        print("-" * 50)


if __name__ == '__main__':
    main()
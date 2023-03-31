'''
Educative: https://www.educative.io/courses/grokking-coding-interview-patterns-python/39zEoZ0DXwn

Given an input string, return all possible permutations of the string.

* All characters in the input string are unique.
* 1 ≤ word.length ≤ 6

input: 'bad'
output: ['bad','bda','abd','adb','dab','dba']
Tree Explanation:
                                       'bad'
            /                            |                   \   
        fix 'b' (ie: swap b-b)       swap b-a            swap b-d
          'bad'                       'abd'                 'dab'
          /   \                       /   \                 /   \ 
         /     \                     /     \               /     \ 
        /       \                   /       \             /       \ 
    fix 'a'   swap a-d         fix 'b'   swap b-d      fix 'a'   swap a-b
    'bad'       'bda'           'abd'     'adb'        'dab'     'dba'

Iterations:
- Starting from the first index as the current string, recursively compute the permutations of the input string.
- Compute the permutation by the current index with every index in the remaining string
- Recurs the computations step by incrementing the current index by 1.
- If we reach the end of the string, store the current string as a permutation
- Finally, return the list of all permutations 
'''

def swap(str, i, j): #swap two characters in a string
    lst = list(str)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

def permute(word, curr_idx, res): #recursively compute the permutations
    if curr_idx == len(word)-1: #Prevents adding duplicate permutations
        res.append(word)
        return
    
    for i in range(curr_idx, len(word)):
        swapped = swap(word, curr_idx, i)
        permute(swapped, curr_idx+1, res)


def permuteWord(word):
    permutations = []
    permute(word, 0, permutations)
    return permutations


def main():

    input_word = ['a', 'ab', 'bad', 'abc', 'abcd']

    for index in range(len(input_word)):
        permuted_words = permuteWord(input_word[index])

        print(index + 1, '.\t Input string: '', input_word[index], ''', sep='')
        print('\t All possible permutations are: ',
              '[', ', '.join(permuted_words), ']', sep='')
        print('-' * 100)


if __name__ == '__main__':
    main()

'''
TC -> O(n!) where n is the length of the input string. 
SC -> O(n) because the space complexity of this solution is dependent on the depth of the recursive call stack. and The maximum depth of recursion is n.
'''
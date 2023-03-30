# Subsets Pattern

## Overview:
The **subsets pattern** is useful in finding the *permutations and combinations* of elements in a data structure.

The idea is to consider the data structure as a set and make a series of subsets from this set. The subsets generated are based on certain conditions that the problem provides us.

This approach makes all the subsets of a given set in O(n*2^n) time, where n is the number of elements in the data structure from which we have to generate subsets.

## Does my problem match this pattern?
- Yes, if the following condition is fulfilled:
    - The problem requires creating permutations or combinations of a given set of elements, either as the final solution, or as an intermediate step.

Additionally, the problem may specify a condition for including a particular permutation or combination in the final solution.

- No, if the following condition is fulfilled:
    - We are not required to generate permutations or combinations of a set of elements.

## Real-world problems:
Many problems in the real world use the subsets pattern. Let’s look at some examples.

- Movie combinations: Create a combination of movies, chosen from the given set of genres in a specific sequence.

- Movie viewing orders: Generate all possible permutations of a given set of movies to provide options for a movie marathon.

- Total cost of shopping items: An equation calculating the total cost of items needs to be divided into subsets of items.
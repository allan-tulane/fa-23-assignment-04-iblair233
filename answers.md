# CMPS 2200 Assignment 4
## Answers

**Name:** Izzy Blair


Place all written answers from `assignment-04.md` here for easier grading.
1a. A greedy algorithm would initialize coin count to 0 and repeat selecting coins of highest power of 2 that are less than or equal to N until we reach N.

1b. It is optimal because the largest coin will always make the remaining change smaller. there will always be a smaller problem next to solve and the best solution for that smallest amount when added to the coins already chosen will assuredly be the best solution.

1c. both work and span are O(logN)

2a. A counterexample that shows that the alrogithm does not produce the fewest number of coins is where the denominations are 4, 3, and 1 for making change for 6 dollars. The algorithm would choose a denomination 4 coin, two denomination 1 coins to get six dollars in three coins. The optimal solution, though, would be to use two coins of denomination 3 to get six dollars with two coins. The greedy algorithm therefore failed because it didn't get the least amount of coins possible.

2b. The optimal substructure property would be that if you know the optimal change making for N dollars, then for any count less than N the solution for that smaller amount has to also be optimal.

2c. Work: (n*k)
Span: O(n)

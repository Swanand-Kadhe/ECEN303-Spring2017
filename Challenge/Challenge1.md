
# Programming Challenge 1

This [Python](https://www.python.org) challenge will use the `random` module to generate pseudo random numbers.
Remember to import this module whenever needed.

```python
import random
```

Write a method to simulate the flipping of a biased (binary) coin.
The method should return a one with probability `p`, and it should return a zero with probability `1-p`.
The argument `p=0.5` signifies that the default value for parameter `p` is 0.5; still, your method should work for any value between zero and one.

```python
def biasedcoinflip(p=0.5):
    # EDIT
    # Create method for biased coin flip
    #
```

Create a method that sums `NumberFlips` outcomes of `biasedcoinflip()` and appends the result to list `SumTrials`.

```python
SumTrials = []

for TrialIndex2 in range(0, NumberTrials):
    # EDIT
    # Add NumberFlips coin flips for each SumTrials outcome
    #
```

Sum the values of all the elements contained in list `Distribution` and print the result.

```python
print repr(Distribution)
# EDIT
# Print the sum of the elements in Distribution
#
```

Address the following three problems.

1. Describe what happens to the figure as you vary `ParameterP` from zero to one.
2. What is the sum of the elements in Distribution? 
3. What is the most likely outcome for `ParameterP = 0.7` and `NumberFlips = 8`?

Place your answers for 2 and 3 in the appropriate variables at the top of the file. The answers should simply be a number. 



## Submission

A template named `1challenge.py` has been placed in your personal folder.
Edit this template and address the two problems at the end.
After completing this programming challenge, fill out the self-grading portion.
Commit your work to our repository using Git and GitHub.



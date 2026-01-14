**Method:** linearity of expectation with indicator variables  
**Key idea:** add up “is position i fixed?” over all i  
**Difficulty:** ★★☆☆☆  
**Sanity check:** try small n like n = 2 or 3

### Problem

Let π be a uniformly random permutation of {1, 2, ..., n}.

A “fixed point” is an index i such that π(i) = i.

What is the expected number of fixed points?

### Solution

Define a random variable Xi for each position i:

- Xi = 1 if π(i) = i,
- Xi = 0 otherwise.

Let X be the total number of fixed points:
X = X1 + X2 + ... + Xn.

We want E[X]. By linearity of expectation:
E[X] = E[X1] + E[X2] + ... + E[Xn].

Now compute E[Xi]. Because the permutation is uniform, the value at position i is equally likely to be any of the n values, so:
P(π(i) = i) = 1 / n.

Then:
E[Xi] = 1 * P(π(i) = i) + 0 * P(π(i) ≠ i) = 1 / n.

So:
E[X] = n * (1 / n) = 1.

### Answer

The expected number of fixed points in a random permutation of n elements is 1.

Sanity check:  
For n = 1, there is always exactly 1 fixed point.  
For n = 2, the permutations are (1,2) with 2 fixed points and (2,1) with 0 fixed points, so the average is (2 + 0)/2 = 1.

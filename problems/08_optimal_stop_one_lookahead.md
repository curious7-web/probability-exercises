**Method:** one-step lookahead with simple comparison  
**Key idea:** compare X to the expected value of Y  
**Difficulty:** ★★☆☆☆  
**Sanity check:** answer should be better than always taking X or always taking Y

### Problem

You will see two independent rolls of a fair six-sided die (values 1–6).

1. First you observe X (the first roll).
2. You must decide to either accept X and stop, or reject X.
3. If you reject X, you are forced to take Y (the second roll), whatever it is.

What strategy maximizes your expected value, and what is that expected value?

### Solution

First compute the expected value of Y:

Y is uniform on {1, 2, 3, 4, 5, 6}, so:
E[Y] = (1 + 2 + 3 + 4 + 5 + 6) / 6 = 21 / 6 = 3.5.

When you see X, your choices are:

- Take X and get value X.
- Reject X and wait for Y, with expected value 3.5.

So the rule is simple:

- If X is at least 3.5, you keep it.
- If X is less than 3.5, you reject it and take Y.

Since X is an integer from 1 to 6:

- Reject X if X ∈ {1, 2, 3}.
- Accept X if X ∈ {4, 5, 6}.

Now compute the expected value under this strategy.

With probability 3/6 = 1/2, X ∈ {1, 2, 3}. In that case we reject and get Y, with expected value 3.5.

With probability 1/2, X ∈ {4, 5, 6}. In that case we accept X, whose conditional expectation is:
E[X | X ∈ {4, 5, 6}] = (4 + 5 + 6) / 3 = 5.

So:
E[value] = (1/2) * 3.5 + (1/2) * 5
         = 1.75 + 2.5
         = 4.25.

### Answer

Optimal strategy: accept the first roll if it is 4, 5, or 6; otherwise reject it and take the second roll.

This strategy gives an expected value of 4.25, which is better than always taking the first roll (expected value 3.5) or always waiting for the second roll (also 3.5).

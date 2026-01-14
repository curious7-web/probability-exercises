**Method:** conditioning on first flip  
**Key idea:** reset after tails  
**Difficulty:** ★☆☆☆☆  
**Sanity check:** p=0.5 gives 2

### Problem

A biased coin shows heads with probability p on each flip. Flips are independent.

What is the expected number of flips until the first heads appears?

### Solution

Let E be the expected number of flips until first heads.

On the first flip:

- With probability p, we see heads and are done in 1 flip.
- With probability (1-p), we see tails, spend 1 flip, and face the same situation again with expectation E.

So:
E = p * 1 + (1-p) * (1 + E)
  = p + (1-p) + (1-p)E
  = 1 + (1-p)E

Thus:
E - (1-p)E = 1
pE = 1
E = 1/p

### Answer

The expected number of flips until the first heads is E = 1/p.

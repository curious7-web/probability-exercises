**Method:** linear equations for expected times  
**Key idea:** from each non-absorbing state, E = 1 + average of neighbors’ E  
**Difficulty:** ★★☆☆☆  
**Sanity check:** starting in the middle should take a few steps, not dozens

### Problem

Consider a random walk on the states {0, 1, 2, 3, 4}.

At each step, from states 1, 2, or 3:

- With probability 1/2 you move to i - 1,
- With probability 1/2 you move to i + 1.

States 0 and 4 are absorbing (once you reach them, you stay there).

If you start at state 2, what is the expected number of steps until absorption (hitting 0 or 4)?

### Solution

Let E_i be the expected number of steps to absorption starting from state i.

We know:
- E_0 = 0 (already absorbed),
- E_4 = 0.

For i = 1, 2, 3, we use one-step conditioning:

From state i, you always take 1 step, then go to i - 1 or i + 1 with equal probability. So:
E_i = 1 + (1/2) * E_{i-1} + (1/2) * E_{i+1}.

Write out the equations:

1) E_1 = 1 + (1/2) * E_0 + (1/2) * E_2 = 1 + (1/2) * E_2.  
2) E_2 = 1 + (1/2) * E_1 + (1/2) * E_3.  
3) E_3 = 1 + (1/2) * E_2 + (1/2) * E_4 = 1 + (1/2) * E_2.

By symmetry, E_1 and E_3 should be equal, and the equations confirm that.

From (1):  
E_1 = 1 + (1/2) * E_2.

Plug E_1 and E_3 = E_1 into (2):

E_2 = 1 + (1/2) * E_1 + (1/2) * E_1  
    = 1 + E_1.

Use E_1 = 1 + (1/2) * E_2:

E_2 = 1 + (1 + (1/2) * E_2)
    = 2 + (1/2) * E_2.

So:
E_2 - (1/2) * E_2 = 2  
(1/2) * E_2 = 2  
E_2 = 4.

### Answer

Starting from state 2, the expected number of steps until absorption is 4.

This is reasonable: you’re in the middle of a short 5-point line, so it should take a small number of steps (not something huge).

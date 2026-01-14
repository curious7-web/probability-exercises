**Method:** linear equations for hitting probabilities  
**Key idea:** from each state, probability is the average of neighbors  
**Difficulty:** ★★☆☆☆  
**Sanity check:** symmetric start, so probability should be 1/2

### Problem

A gambler starts with 2 dollars and plays a fair game:

- Each round, they either win 1 dollar with probability 1/2, or
- lose 1 dollar with probability 1/2.

The game ends when their fortune hits 0 dollars (ruin) or 4 dollars (target).

What is the probability that the gambler reaches 4 dollars before 0 dollars?

### Solution

Let p_i be the probability of eventually reaching 4 before 0 if the gambler currently has i dollars.

We want p_2.

Boundary conditions:
- p_0 = 0  (if you’re at 0, you’re ruined already),
- p_4 = 1  (if you’re at 4, you’ve already hit the target).

For i = 1, 2, 3 we condition on the next round. From state i:

- With probability 1/2 you go to i - 1,
- With probability 1/2 you go to i + 1.

So:
p_i = (1/2) * p_{i-1} + (1/2) * p_{i+1}.

Write out the equations:

1) p_1 = (1/2) * p_0 + (1/2) * p_2 = (1/2) * p_2.  
2) p_2 = (1/2) * p_1 + (1/2) * p_3.  
3) p_3 = (1/2) * p_2 + (1/2) * p_4 = (1/2) * p_2 + 1/2.

Now substitute (1) and (3) into (2):

p_2 = (1/2) * p_1 + (1/2) * p_3  
    = (1/2) * (1/2 * p_2) + (1/2) * ((1/2) * p_2 + 1/2)  
    = (1/4) * p_2 + (1/4) * p_2 + 1/4  
    = (1/2) * p_2 + 1/4.

Move terms:

p_2 - (1/2) * p_2 = 1/4  
(1/2) * p_2 = 1/4  
p_2 = 1/2.

### Answer

Starting from 2 dollars, the probability of hitting 4 dollars before 0 is 1/2.

This is also intuitive: the start (2) is exactly in the middle of 0 and 4 in a fair random walk, so hitting either boundary first is symmetric.

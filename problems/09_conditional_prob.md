**Method:** list outcomes and condition on allowed ones  
**Key idea:** throw away the case that violates the condition  
**Difficulty:** ★★☆☆☆  
**Sanity check:** answer should be between 0 and 1 and not obviously 1/2

### Problem

A family has two children. Each child is equally likely to be a boy or a girl, independently.

Given that at least one of the children is a boy, what is the probability that both children are boys?

### Solution

List all equally likely possibilities for the two children in order (older, younger):

- BB
- BG
- GB
- GG

Each has probability 1/4.

Now use the condition “at least one is a boy”. That rules out the case GG.

So the possible cases under this condition are:
BB, BG, GB.

They are still equally likely, so each has probability 1/3 given the condition.

Among these three cases, only BB has both children as boys.

So:
P(both boys | at least one boy) = 1/3.

### Answer

Given that at least one child is a boy, the probability that both are boys is 1/3.

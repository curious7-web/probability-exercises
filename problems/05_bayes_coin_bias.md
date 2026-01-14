**Method:** Bayes’ rule over two simple models  
**Key idea:** compare how likely HHH is under each coin  
**Difficulty:** ★★☆☆☆  
**Sanity check:** answer should be > 0.5 because HHH is more likely with the biased coin

### Problem

You have two coins:

- Coin A: fair, with P(H) = 1/2.
- Coin B: biased, with P(H) = 3/4.

You pick one coin at random (each with probability 1/2), then flip it 3 times and see HHH (three heads).

What is the probability that you picked the biased coin, given this observation?

### Solution

Let:
- F = event “picked fair coin A”,
- B = event “picked biased coin B”,
- HHH = event “got three heads in a row”.

We want P(B | HHH).

By Bayes’ rule:
P(B | HHH) = P(HHH | B) * P(B) / P(HHH).

We know:
P(B) = 1/2 and P(F) = 1/2.

Compute the likelihoods:

- If the coin is fair: P(HHH | F) = (1/2)^3 = 1/8.
- If the coin is biased: P(HHH | B) = (3/4)^3 = 27/64.

Now use total probability for HHH:

P(HHH) = P(HHH | F) * P(F) + P(HHH | B) * P(B)
       = (1/8) * (1/2) + (27/64) * (1/2)
       = 1/16 + 27/128
       = 8/128 + 27/128
       = 35/128.

Now plug into Bayes:

P(B | HHH) = (P(HHH | B) * P(B)) / P(HHH)
           = (27/64 * 1/2) / (35/128)
           = (27/128) / (35/128)
           = 27/35.

### Answer

Given three heads in a row, the posterior probability that the coin was the biased one is 27/35, which is about 0.77.

This is > 0.5 as expected, because HHH is more likely with the biased coin.

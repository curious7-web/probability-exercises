**Method:** small state machine (scratch vs last was H)  
**Key idea:** track whether the previous flip was a head  
**Difficulty:** ★★☆☆☆  
**Sanity check:** small simulation (see code/hh_sim.py)

### Problem

You flip a fair coin repeatedly (heads with probability 1/2 each flip).

What is the expected number of flips until you see two heads in a row (HH)?

### Solution

I’ll use two states:

- E = expected number of flips starting from scratch (we don’t care about the last flip).
- E_H = expected number of flips given that the last flip was heads.

We want E.

**From scratch (E)**

On the next flip:

- With probability 1/2, we get tails. We used 1 flip and we’re still in the “scratch” situation, so expected remaining flips is E again.
- With probability 1/2, we get heads. We used 1 flip and now we’re in the “last was H” state, which has expectation E_H.

So:
E = 1 + (1/2) * E + (1/2) * E_H.

**From last was H (E_H)**

Now suppose the last flip was H.

- With probability 1/2, the next flip is heads again. That gives HH and we are done after 1 more flip.
- With probability 1/2, the next flip is tails. We used 1 flip and go back to scratch, so expectation E.

So:
E_H = 1 + (1/2) * 0 + (1/2) * E
    = 1 + (1/2) * E.

**Solve the two equations**

From the first equation:
E - (1/2) * E = 1 + (1/2) * E_H  
(1/2) * E = 1 + (1/2) * E_H  
E = 2 + E_H.

From the second equation:
E_H = 1 + (1/2) * E.

Plug E = 2 + E_H into that:
E_H = 1 + (1/2) * (2 + E_H)
    = 1 + 1 + (1/2) * E_H
    = 2 + (1/2) * E_H.

So:
E_H - (1/2) * E_H = 2  
(1/2) * E_H = 2  
E_H = 4.

Then:
E = 2 + E_H = 2 + 4 = 6.

### Answer

On average, it takes 6 flips to see two heads in a row for a fair coin.

A quick simulation (see code/hh_sim.py) gives an average close to 6, which matches this result.

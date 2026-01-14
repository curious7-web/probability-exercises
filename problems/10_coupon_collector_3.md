**Method:** state-based expectation  
**Key idea:** track how many distinct coupons you already have  
**Difficulty:** ★★☆☆☆  
**Sanity check:** small simulation (see code/coupon_sim.py)

### Problem

There are 3 types of coupons. Each time you draw a coupon, it is equally likely to be any of the 3 types, independent of past draws.

What is the expected number of draws needed to collect all 3 distinct types at least once?

### Solution

Define:

- E0 = expected number of additional draws when you have 0 distinct types.
- E1 = expected number of additional draws when you have 1 distinct type.
- E2 = expected number of additional draws when you have 2 distinct types.
- E3 = 0, because if you already have all 3, you are done.

We want E0.

**State with 2 types (E2)**

Suppose you already have 2 distinct types and are missing 1 type.

On the next draw:

- With probability 1/3, you get the missing type and finish.
- With probability 2/3, you get one of the types you already have and stay in the same state (still 2 types).

So:
E2 = 1 + (2/3) * E2 + (1/3) * 0.

Rearrange:
E2 - (2/3) * E2 = 1  
(1/3) * E2 = 1  
E2 = 3.

**State with 1 type (E1)**

Now suppose you have exactly 1 distinct type.

On the next draw:

- With probability 1/3, you draw that same type and stay at 1 distinct type.
- With probability 2/3, you draw a new type and move to the “2 types” state.

So:
E1 = 1 + (1/3) * E1 + (2/3) * E2.

Bring terms together:
E1 - (1/3) * E1 = 1 + (2/3) * E2  
(2/3) * E1 = 1 + (2/3) * 3  
(2/3) * E1 = 1 + 2 = 3.

So:
E1 = 3 / (2/3) = 3 * (3/2) = 9/2 = 4.5.

**State with 0 types (E0)**

If you have 0 types, the very first draw always gives you a new type (there is nothing to repeat), so after 1 draw you are in the E1 state:

E0 = 1 + E1 = 1 + 4.5 = 5.5.

### Answer

The expected number of draws to collect all 3 coupon types is 5.5.

A quick simulation (see code/coupon_sim.py) gives an average close to 5.5 across many trials.
